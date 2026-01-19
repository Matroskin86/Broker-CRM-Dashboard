import reflex as rx
from app.states.dashboard_state import DashboardState


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="h-5 w-5 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2",
                    ),
                    rx.el.input(
                        type="text",
                        placeholder="Search clients, deals, or reminders...",
                        on_change=DashboardState.set_search_query,
                        class_name="pl-10 pr-4 py-2 w-full md:w-96 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent bg-gray-50 hover:bg-white transition-colors placeholder-gray-400",
                        default_value=DashboardState.search_query,
                    ),
                    rx.el.div(
                        rx.el.span(
                            "⌘", class_name="text-xs text-gray-400 font-medium mr-1"
                        ),
                        rx.el.span("K", class_name="text-xs text-gray-400 font-medium"),
                        class_name="hidden md:flex absolute right-3 top-1/2 transform -translate-y-1/2 border border-gray-200 rounded px-1.5 py-0.5 bg-white shadow-sm",
                    ),
                    class_name="relative",
                ),
                class_name="flex-1 flex items-center",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "bell", size=20, class_name="text-gray-500 hover:text-gray-700"
                    ),
                    class_name="p-2 rounded-full hover:bg-gray-100 transition-colors relative",
                ),
                rx.el.div(
                    rx.el.span(
                        class_name="absolute top-2 right-2 h-2 w-2 rounded-full bg-red-500 border-2 border-white"
                    ),
                    class_name="relative",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.image(
                            src="https://api.dicebear.com/9.x/avataaars/svg?seed=Felix",
                            class_name="h-8 w-8 rounded-full ring-2 ring-white",
                        ),
                        on_click=DashboardState.toggle_profile,
                        class_name="ml-4 focus:outline-none",
                    ),
                    rx.cond(
                        DashboardState.is_profile_open,
                        rx.el.div(
                            rx.el.div(
                                rx.el.a(
                                    "Your Profile",
                                    href="#",
                                    class_name="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100",
                                ),
                                rx.el.a(
                                    "Settings",
                                    href="#",
                                    class_name="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100",
                                ),
                                rx.el.a(
                                    "Sign out",
                                    href="#",
                                    class_name="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100",
                                ),
                                class_name="py-1",
                            ),
                            class_name="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none z-50 animate-in fade-in zoom-in-95 duration-100",
                        ),
                    ),
                    class_name="relative",
                ),
                class_name="flex items-center space-x-2",
            ),
            class_name="flex justify-between h-16 px-6 md:px-8 border-b border-gray-200 bg-white items-center sticky top-0 z-20",
        ),
        class_name="bg-white",
    )