import reflex as rx
from typing import TypedDict, Optional
import random
import string
from datetime import datetime


class Reminder(TypedDict):
    id: str
    client_id: str
    client_name: str
    message: str
    scheduled_date: str
    status: str
    type: str


class ReminderState(rx.State):
    """State management for the reminders system."""

    reminders: list[Reminder] = [
        {
            "id": "1",
            "client_id": "1",
            "client_name": "TechFlow Systems",
            "message": "Follow up on the Q3 proposal",
            "scheduled_date": "2024-03-20",
            "status": "Pending",
            "type": "Call",
        },
        {
            "id": "2",
            "client_id": "3",
            "client_name": "Global Dynamics",
            "message": "Send revised contract draft",
            "scheduled_date": "2024-03-22",
            "status": "Pending",
            "type": "Email",
        },
        {
            "id": "3",
            "client_id": "2",
            "client_name": "Pearson Legal",
            "message": "Lunch meeting to discuss expansion",
            "scheduled_date": "2024-03-15",
            "status": "Completed",
            "type": "Meeting",
        },
    ]
    is_modal_open: bool = False
    modal_mode: str = "add"
    selected_client_id: str = ""
    selected_client_name: str = ""
    current_reminder: Reminder = {
        "id": "",
        "client_id": "",
        "client_name": "",
        "message": "",
        "scheduled_date": "",
        "status": "Pending",
        "type": "Call",
    }

    @rx.event
    def open_add_modal(self):
        """Open modal to add a generic reminder."""
        self.modal_mode = "add"
        self.selected_client_id = ""
        self.selected_client_name = ""
        self.current_reminder = {
            "id": "",
            "client_id": "",
            "client_name": "",
            "message": "",
            "scheduled_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "Pending",
            "type": "Call",
        }
        self.is_modal_open = True

    @rx.event
    def open_add_modal_for_client(self, client: dict):
        """Open modal to add a reminder for a specific client."""
        self.modal_mode = "add"
        self.selected_client_id = client["id"]
        self.selected_client_name = client["name"]
        self.current_reminder = {
            "id": "",
            "client_id": client["id"],
            "client_name": client["name"],
            "message": "",
            "scheduled_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "Pending",
            "type": "Call",
        }
        self.is_modal_open = True

    @rx.event
    def open_edit_modal(self, reminder: Reminder):
        """Open modal to edit an existing reminder."""
        self.modal_mode = "edit"
        self.current_reminder = reminder
        self.selected_client_id = reminder["client_id"]
        self.selected_client_name = reminder["client_name"]
        self.is_modal_open = True

    @rx.event
    def close_modal(self):
        self.is_modal_open = False

    @rx.event
    async def handle_save_reminder(self, form_data: dict):
        """Save new or updated reminder."""
        client_id = form_data.get("client_id")
        client_name = ""
        from app.states.client_state import ClientState

        client_state = await self.get_state(ClientState)
        for client in client_state.clients:
            if client["id"] == client_id:
                client_name = client["name"]
                break
        if self.modal_mode == "add":
            new_reminder: Reminder = {
                "id": "".join(
                    random.choices(string.ascii_letters + string.digits, k=8)
                ),
                "client_id": client_id,
                "client_name": client_name,
                "message": form_data.get("message", ""),
                "scheduled_date": form_data.get("scheduled_date", ""),
                "status": "Pending",
                "type": form_data.get("type", "Call"),
            }
            self.reminders.insert(0, new_reminder)
            yield rx.toast("Reminder scheduled successfully.")
        elif self.modal_mode == "edit":
            updated_list = []
            for r in self.reminders:
                if r["id"] == form_data.get("id"):
                    updated_r = r.copy()
                    updated_r.update(
                        {
                            "client_id": client_id,
                            "client_name": client_name,
                            "message": form_data.get("message", r["message"]),
                            "scheduled_date": form_data.get(
                                "scheduled_date", r["scheduled_date"]
                            ),
                            "type": form_data.get("type", r["type"]),
                        }
                    )
                    updated_list.append(updated_r)
                else:
                    updated_list.append(r)
            self.reminders = updated_list
            yield rx.toast("Reminder updated.")
        self.is_modal_open = False

    @rx.event
    def delete_reminder(self, reminder_id: str):
        self.reminders = [r for r in self.reminders if r["id"] != reminder_id]
        yield rx.toast("Reminder deleted.")

    @rx.event
    def mark_as_sent(self, reminder_id: str):
        updated_list = []
        for r in self.reminders:
            if r["id"] == reminder_id:
                updated_r = r.copy()
                updated_r["status"] = "Sent"
                updated_list.append(updated_r)
            else:
                updated_list.append(r)
        self.reminders = updated_list
        yield rx.toast("Marked as sent.")

    @rx.event
    def mark_as_completed(self, reminder_id: str):
        updated_list = []
        for r in self.reminders:
            if r["id"] == reminder_id:
                updated_r = r.copy()
                updated_r["status"] = "Completed"
                updated_list.append(updated_r)
            else:
                updated_list.append(r)
        self.reminders = updated_list
        yield rx.toast("Marked as completed.")