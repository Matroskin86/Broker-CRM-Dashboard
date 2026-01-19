import reflex as rx
from app.states.dashboard_state import DashboardState


def nav_item(item: str) -> rx.Component:
    is_active = DashboardState.active_tab == item
    icon_map = {
        "Dashboard": "layout-dashboard",
        "Clients": "users",
        "Reminders": "bell",
    }
    return rx.el.button(
        rx.icon(
            rx.match(
                item,
                ("Dashboard", "layout-dashboard"),
                ("Clients", "users"),
                ("Reminders", "bell"),
                "circle",
            ),
            class_name=rx.cond(
                is_active, "text-teal-600", "text-gray-400 group-hover:text-gray-500"
            ),
            size=20,
        ),
        rx.el.span(item, class_name="ml-3 text-sm font-medium"),
        on_click=lambda: DashboardState.set_active_tab(item),
        class_name=rx.cond(
            is_active,
            "flex items-center w-full px-3 py-2 rounded-lg bg-teal-50 text-teal-700 transition-colors group",
            "flex items-center w-full px-3 py-2 rounded-lg text-gray-700 hover:bg-gray-100 transition-colors group",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "hexagon", class_name="text-teal-600 h-8 w-8", stroke_width=2.5
                ),
                rx.el.span(
                    "BrokerFlow",
                    class_name="ml-2 text-xl font-bold text-gray-900 tracking-tight",
                ),
                class_name="flex items-center px-2",
            ),
            class_name="h-16 flex items-center px-4 border-b border-gray-100",
        ),
        rx.el.div(
            rx.el.nav(
                rx.el.div(
                    rx.el.p(
                        "MAIN",
                        class_name="px-3 text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2 mt-2",
                    ),
                    rx.foreach(DashboardState.nav_items, nav_item),
                    class_name="space-y-1",
                ),
                class_name="flex-1 px-2 py-4 space-y-4",
            ),
            class_name="flex flex-col flex-1 overflow-y-auto",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src="https://api.dicebear.com/9.x/avataaars/svg?seed=Felix",
                        class_name="h-9 w-9 rounded-full bg-gray-50",
                    ),
                    class_name="flex-shrink-0",
                ),
                rx.el.div(
                    rx.el.p(
                        "Felix Vance", class_name="text-sm font-medium text-gray-700"
                    ),
                    rx.el.p("Senior Broker", class_name="text-xs text-gray-500"),
                    class_name="ml-3",
                ),
                class_name="flex items-center",
            ),
            class_name="p-4 border-t border-gray-100",
        ),
        class_name="hidden md:flex flex-col w-64 bg-white border-r border-gray-200 h-screen fixed left-0 top-0 z-30",
    )