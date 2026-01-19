import reflex as rx
from typing import TypedDict
import random
import string


class Client(TypedDict):
    id: str
    name: str
    email: str
    phone: str
    status: str
    deal_value: int
    last_contact: str
    avatar_seed: str


class ClientState(rx.State):
    """State management for the clients page."""

    clients: list[Client] = [
        {
            "id": "1",
            "name": "TechFlow Systems",
            "email": "contact@techflow.com",
            "phone": "+1 (555) 123-4567",
            "status": "Active",
            "deal_value": 125000,
            "last_contact": "2024-03-10",
            "avatar_seed": "techflow",
        },
        {
            "id": "2",
            "name": "Pearson Legal",
            "email": "j.pearson@pearsonlegal.com",
            "phone": "+1 (555) 987-6543",
            "status": "Pending",
            "deal_value": 45000,
            "last_contact": "2024-03-12",
            "avatar_seed": "pearson",
        },
        {
            "id": "3",
            "name": "Global Dynamics",
            "email": "info@globaldynamics.net",
            "phone": "+1 (555) 456-7890",
            "status": "Closed",
            "deal_value": 850000,
            "last_contact": "2024-02-28",
            "avatar_seed": "global",
        },
        {
            "id": "4",
            "name": "Velcro Corp",
            "email": "sales@velcrocorp.com",
            "phone": "+1 (555) 222-3333",
            "status": "Lost",
            "deal_value": 15000,
            "last_contact": "2024-01-15",
            "avatar_seed": "velcro",
        },
        {
            "id": "5",
            "name": "Summit Financial",
            "email": "finance@summit.com",
            "phone": "+1 (555) 777-8888",
            "status": "Active",
            "deal_value": 320000,
            "last_contact": "2024-03-14",
            "avatar_seed": "summit",
        },
    ]
    search_query: str = ""
    status_filter: str = "All"
    is_modal_open: bool = False
    modal_mode: str = "add"
    selected_client: Client = {
        "id": "",
        "name": "",
        "email": "",
        "phone": "",
        "status": "Active",
        "deal_value": 0,
        "last_contact": "",
        "avatar_seed": "",
    }

    @rx.var
    def filtered_clients(self) -> list[Client]:
        """Filter clients based on search query and status."""
        filtered = self.clients
        if self.status_filter != "All":
            filtered = [c for c in filtered if c["status"] == self.status_filter]
        if self.search_query:
            query = self.search_query.lower()
            filtered = [
                c
                for c in filtered
                if query in c["name"].lower() or query in c["email"].lower()
            ]
        return filtered

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def set_status_filter(self, status: str):
        self.status_filter = status

    @rx.event
    def open_add_modal(self):
        self.modal_mode = "add"
        self.selected_client = {
            "id": "",
            "name": "",
            "email": "",
            "phone": "",
            "status": "Active",
            "deal_value": 0,
            "last_contact": "",
            "avatar_seed": "",
        }
        self.is_modal_open = True

    @rx.event
    def open_edit_modal(self, client: Client):
        self.modal_mode = "edit"
        self.selected_client = client
        self.is_modal_open = True

    @rx.event
    def open_view_modal(self, client: Client):
        self.modal_mode = "view"
        self.selected_client = client
        self.is_modal_open = True

    @rx.event
    def close_modal(self):
        self.is_modal_open = False

    @rx.event
    def handle_save_client(self, form_data: dict):
        if self.modal_mode == "add":
            new_client: Client = {
                "id": "".join(
                    random.choices(string.ascii_letters + string.digits, k=8)
                ),
                "name": form_data.get("name", ""),
                "email": form_data.get("email", ""),
                "phone": form_data.get("phone", ""),
                "status": form_data.get("status", "Active"),
                "deal_value": int(form_data.get("deal_value", 0)),
                "last_contact": form_data.get("last_contact", ""),
                "avatar_seed": form_data.get("name", "default")
                .replace(" ", "")
                .lower(),
            }
            self.clients.insert(0, new_client)
            yield rx.toast(f"Client {new_client['name']} added successfully.")
        elif self.modal_mode == "edit":
            client_id = form_data.get("id")
            updated_list = []
            for client in self.clients:
                if client["id"] == client_id:
                    updated_client = client.copy()
                    updated_client.update(
                        {
                            "name": form_data.get("name", client["name"]),
                            "email": form_data.get("email", client["email"]),
                            "phone": form_data.get("phone", client["phone"]),
                            "status": form_data.get("status", client["status"]),
                            "deal_value": int(
                                form_data.get("deal_value", client["deal_value"])
                            ),
                            "last_contact": form_data.get(
                                "last_contact", client["last_contact"]
                            ),
                        }
                    )
                    updated_list.append(updated_client)
                else:
                    updated_list.append(client)
            self.clients = updated_list
            yield rx.toast("Client details updated.")
        self.is_modal_open = False

    @rx.event
    def delete_client(self, client_id: str):
        self.clients = [c for c in self.clients if c["id"] != client_id]
        self.is_modal_open = False
        yield rx.toast("Client removed.")

    @rx.event
    def send_reminder_toast(self):
        yield rx.toast(f"Reminder sent to {self.selected_client['name']}")