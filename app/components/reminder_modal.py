import reflex as rx
from app.states.reminder_state import ReminderState
from app.states.client_state import ClientState


def reminder_modal() -> rx.Component:
    return rx.cond(
        ReminderState.is_modal_open,
        rx.el.div(
            rx.el.div(
                class_name="fixed inset-0 bg-gray-500/75 transition-opacity z-40",
                on_click=ReminderState.close_modal,
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                rx.cond(
                                    ReminderState.modal_mode == "add",
                                    "Schedule Reminder",
                                    "Edit Reminder",
                                ),
                                class_name="text-lg font-semibold leading-6 text-gray-900",
                            ),
                            rx.el.button(
                                rx.icon(
                                    "x",
                                    size=20,
                                    class_name="text-gray-400 hover:text-gray-500",
                                ),
                                on_click=ReminderState.close_modal,
                            ),
                            class_name="flex items-center justify-between mb-6",
                        ),
                        rx.el.form(
                            rx.el.input(
                                type="hidden",
                                name="id",
                                value=ReminderState.current_reminder["id"],
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Client",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.select(
                                    rx.el.option(
                                        "Select a client", value="", disabled=True
                                    ),
                                    rx.foreach(
                                        ClientState.clients,
                                        lambda client: rx.el.option(
                                            client["name"], value=client["id"]
                                        ),
                                    ),
                                    name="client_id",
                                    default_value=rx.cond(
                                        ReminderState.current_reminder["client_id"]
                                        != "",
                                        ReminderState.current_reminder["client_id"],
                                        ReminderState.selected_client_id,
                                    ),
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent disabled:bg-gray-50 disabled:text-gray-500",
                                ),
                                class_name="mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Reminder Type",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.select(
                                    rx.el.option("Call", value="Call"),
                                    rx.el.option("Email", value="Email"),
                                    rx.el.option("Meeting", value="Meeting"),
                                    name="type",
                                    default_value=ReminderState.current_reminder[
                                        "type"
                                    ],
                                    class_name="w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent",
                                ),
                                class_name="mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Message / Note",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.textarea(
                                    name="message",
                                    default_value=ReminderState.current_reminder[
                                        "message"
                                    ],
                                    placeholder="What needs to be done?",
                                    rows=3,
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent",
                                ),
                                class_name="mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Scheduled Date",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.input(
                                    type="date",
                                    name="scheduled_date",
                                    default_value=ReminderState.current_reminder[
                                        "scheduled_date"
                                    ],
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent",
                                ),
                                class_name="mb-6",
                            ),
                            rx.el.div(
                                rx.el.button(
                                    "Cancel",
                                    type="button",
                                    on_click=ReminderState.close_modal,
                                    class_name="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500 mr-3",
                                ),
                                rx.el.button(
                                    "Save Reminder",
                                    type="submit",
                                    class_name="px-4 py-2 text-sm font-medium text-white bg-teal-600 border border-transparent rounded-lg hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500",
                                ),
                                class_name="flex justify-end pt-6 border-t border-gray-100",
                            ),
                            on_submit=ReminderState.handle_save_reminder,
                        ),
                        class_name="relative transform overflow-hidden rounded-xl bg-white p-6 text-left shadow-xl transition-all w-full max-w-md",
                    ),
                    class_name="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0",
                ),
                class_name="fixed inset-0 z-50 w-screen overflow-y-auto",
            ),
            class_name="relative z-50",
        ),
    )