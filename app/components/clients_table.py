import reflex as rx
from app.states.client_state import ClientState, Client
from app.states.reminder_state import ReminderState


def status_badge(status: str) -> rx.Component:
    return rx.match(
        status,
        (
            "Active",
            rx.el.span(
                "Active",
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800",
            ),
        ),
        (
            "Pending",
            rx.el.span(
                "Pending",
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-amber-100 text-amber-800",
            ),
        ),
        (
            "Closed",
            rx.el.span(
                "Closed",
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800",
            ),
        ),
        (
            "Lost",
            rx.el.span(
                "Lost",
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800",
            ),
        ),
        rx.el.span(
            status,
            class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800",
        ),
    )


def client_row(client: Client) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={client['avatar_seed']}",
                    class_name="h-10 w-10 rounded-full bg-gray-100",
                ),
                rx.el.div(
                    rx.el.div(client["name"], class_name="font-medium text-gray-900"),
                    rx.el.div(client["email"], class_name="text-gray-500 text-xs"),
                    class_name="ml-4",
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            client["phone"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            status_badge(client["status"]), class_name="px-6 py-4 whitespace-nowrap"
        ),
        rx.el.td(
            rx.el.span("$", client["deal_value"].to_string()),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-medium",
        ),
        rx.el.td(
            client["last_contact"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "eye", size=18, class_name="text-gray-400 hover:text-teal-600"
                    ),
                    on_click=lambda: ClientState.open_view_modal(client),
                    class_name="p-1 rounded hover:bg-gray-100",
                ),
                rx.el.button(
                    rx.icon(
                        "pencil",
                        size=18,
                        class_name="text-gray-400 hover:text-blue-600",
                    ),
                    on_click=lambda: ClientState.open_edit_modal(client),
                    class_name="p-1 rounded hover:bg-gray-100",
                ),
                rx.el.button(
                    rx.icon(
                        "bell-plus",
                        size=18,
                        class_name="text-gray-400 hover:text-amber-600",
                    ),
                    on_click=lambda: ReminderState.open_add_modal_for_client(client),
                    class_name="p-1 rounded hover:bg-gray-100",
                ),
                class_name="flex space-x-2",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
        class_name="hover:bg-gray-50 transition-colors",
    )


def clients_table() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Clients Directory", class_name="text-xl font-bold text-gray-900"
                ),
                rx.el.p(
                    "Manage your client relationships and deal statuses.",
                    class_name="text-sm text-gray-500 mt-1",
                ),
                class_name="flex flex-col",
            ),
            rx.el.button(
                rx.icon("plus", size=20, class_name="mr-2"),
                "Add Client",
                on_click=ClientState.open_add_modal,
                class_name="flex items-center px-4 py-2 bg-teal-600 text-white rounded-lg hover:bg-teal-700 transition-colors shadow-sm text-sm font-medium",
            ),
            class_name="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    size=18,
                    class_name="text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2",
                ),
                rx.el.input(
                    placeholder="Search by name or email...",
                    on_change=ClientState.set_search_query,
                    class_name="pl-10 pr-4 py-2 w-full border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent",
                ),
                class_name="relative w-full md:w-72",
            ),
            rx.el.div(
                rx.icon(
                    "filter",
                    size=18,
                    class_name="text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2",
                ),
                rx.el.select(
                    rx.el.option("All Statuses", value="All"),
                    rx.el.option("Active", value="Active"),
                    rx.el.option("Pending", value="Pending"),
                    rx.el.option("Closed", value="Closed"),
                    rx.el.option("Lost", value="Lost"),
                    on_change=ClientState.set_status_filter,
                    class_name="pl-10 pr-8 py-2 w-full md:w-48 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent appearance-none bg-white",
                ),
                class_name="relative w-full md:w-auto",
            ),
            class_name="flex flex-col md:flex-row gap-3 mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Client",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Phone",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Deal Value",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Last Contact",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    ),
                    class_name="bg-gray-50 border-b border-gray-200",
                ),
                rx.el.tbody(
                    rx.foreach(ClientState.filtered_clients, client_row),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="overflow-x-auto rounded-xl border border-gray-200 shadow-sm bg-white",
        ),
        rx.cond(
            ClientState.filtered_clients.length() == 0,
            rx.el.div(
                rx.icon("search-x", size=48, class_name="text-gray-300 mb-4"),
                rx.el.p(
                    "No clients found matching your filters.",
                    class_name="text-gray-500 font-medium",
                ),
                class_name="flex flex-col items-center justify-center p-12 bg-white rounded-xl border border-gray-200 mt-4 text-center",
            ),
        ),
    )