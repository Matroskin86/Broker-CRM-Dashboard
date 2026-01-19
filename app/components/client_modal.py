import reflex as rx
from app.states.client_state import ClientState
from app.states.reminder_state import ReminderState


def form_field(
    label: str,
    name: str,
    type: str = "text",
    placeholder: str = "",
    default_value: str = "",
    disabled: bool = False,
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            type=type,
            name=name,
            placeholder=placeholder,
            default_value=default_value,
            disabled=disabled,
            required=True,
            class_name="w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent disabled:bg-gray-50 disabled:text-gray-500",
        ),
        class_name="mb-4",
    )


def status_select(default_value: str, disabled: bool = False) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            "Status", class_name="block text-sm font-medium text-gray-700 mb-1"
        ),
        rx.el.select(
            rx.el.option("Active", value="Active"),
            rx.el.option("Pending", value="Pending"),
            rx.el.option("Closed", value="Closed"),
            rx.el.option("Lost", value="Lost"),
            name="status",
            default_value=default_value,
            disabled=disabled,
            class_name="w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent disabled:bg-gray-50 disabled:text-gray-500",
        ),
        class_name="mb-4",
    )


def client_modal() -> rx.Component:
    return rx.cond(
        ClientState.is_modal_open,
        rx.el.div(
            rx.el.div(
                class_name="fixed inset-0 bg-gray-500/75 transition-opacity z-40",
                on_click=ClientState.close_modal,
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                rx.match(
                                    ClientState.modal_mode,
                                    ("add", "Add New Client"),
                                    ("edit", "Edit Client"),
                                    ("view", "Client Details"),
                                    "Client Details",
                                ),
                                class_name="text-lg font-semibold leading-6 text-gray-900",
                            ),
                            rx.el.button(
                                rx.icon(
                                    "x",
                                    size=20,
                                    class_name="text-gray-400 hover:text-gray-500",
                                ),
                                on_click=ClientState.close_modal,
                            ),
                            class_name="flex items-center justify-between mb-6",
                        ),
                        rx.el.form(
                            rx.el.input(
                                type="hidden",
                                name="id",
                                value=ClientState.selected_client["id"],
                            ),
                            rx.el.div(
                                form_field(
                                    "Company Name",
                                    "name",
                                    default_value=ClientState.selected_client["name"],
                                    placeholder="e.g. Acme Corp",
                                    disabled=ClientState.modal_mode == "view",
                                ),
                                form_field(
                                    "Email Address",
                                    "email",
                                    type="email",
                                    default_value=ClientState.selected_client["email"],
                                    placeholder="contact@example.com",
                                    disabled=ClientState.modal_mode == "view",
                                ),
                                class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                            ),
                            rx.el.div(
                                form_field(
                                    "Phone Number",
                                    "phone",
                                    type="tel",
                                    default_value=ClientState.selected_client["phone"],
                                    placeholder="+1 (555) 000-0000",
                                    disabled=ClientState.modal_mode == "view",
                                ),
                                status_select(
                                    default_value=ClientState.selected_client["status"],
                                    disabled=ClientState.modal_mode == "view",
                                ),
                                class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                            ),
                            rx.el.div(
                                form_field(
                                    "Deal Value ($)",
                                    "deal_value",
                                    type="number",
                                    default_value=ClientState.selected_client[
                                        "deal_value"
                                    ].to_string(),
                                    placeholder="0.00",
                                    disabled=ClientState.modal_mode == "view",
                                ),
                                form_field(
                                    "Last Contact",
                                    "last_contact",
                                    type="date",
                                    default_value=ClientState.selected_client[
                                        "last_contact"
                                    ],
                                    disabled=ClientState.modal_mode == "view",
                                ),
                                class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                            ),
                            rx.el.div(
                                rx.cond(
                                    ClientState.modal_mode != "view",
                                    rx.el.div(
                                        rx.el.button(
                                            "Cancel",
                                            type="button",
                                            on_click=ClientState.close_modal,
                                            class_name="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500 mr-3",
                                        ),
                                        rx.el.button(
                                            "Save Client",
                                            type="submit",
                                            class_name="px-4 py-2 text-sm font-medium text-white bg-teal-600 border border-transparent rounded-lg hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500",
                                        ),
                                        class_name="flex justify-end",
                                    ),
                                    rx.el.div(
                                        rx.el.button(
                                            "Delete Client",
                                            type="button",
                                            on_click=lambda: ClientState.delete_client(
                                                ClientState.selected_client["id"]
                                            ),
                                            class_name="px-4 py-2 text-sm font-medium text-red-700 bg-white border border-red-300 rounded-lg hover:bg-red-50 mr-auto",
                                        ),
                                        rx.el.button(
                                            "Send Reminder",
                                            type="button",
                                            on_click=lambda: ReminderState.open_add_modal_for_client(
                                                ClientState.selected_client
                                            ),
                                            class_name="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 mr-3",
                                        ),
                                        rx.el.button(
                                            "Edit",
                                            type="button",
                                            on_click=lambda: ClientState.open_edit_modal(
                                                ClientState.selected_client
                                            ),
                                            class_name="px-4 py-2 text-sm font-medium text-white bg-teal-600 border border-transparent rounded-lg hover:bg-teal-700",
                                        ),
                                        class_name="flex justify-end w-full",
                                    ),
                                ),
                                class_name="mt-6 pt-6 border-t border-gray-100",
                            ),
                            on_submit=ClientState.handle_save_client,
                            key=ClientState.selected_client["id"].to_string()
                            + ClientState.modal_mode,
                        ),
                        class_name="relative transform overflow-hidden rounded-xl bg-white p-6 text-left shadow-xl transition-all w-full max-w-2xl",
                    ),
                    class_name="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0",
                ),
                class_name="fixed inset-0 z-50 w-screen overflow-y-auto",
            ),
            class_name="relative z-50",
        ),
    )