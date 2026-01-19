import reflex as rx
from app.states.dashboard_state import DashboardState, ActivityItem


def activity_item(item: ActivityItem) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=f"https://api.dicebear.com/9.x/notionists/svg?seed={item['avatar_seed']}",
                class_name="h-10 w-10 rounded-full bg-gray-100 border border-gray-200",
            ),
            rx.el.div(
                rx.el.p(
                    rx.el.span(item["name"], class_name="font-semibold text-gray-900"),
                    rx.el.span(f" {item['action']} ", class_name="text-gray-500"),
                    rx.el.span(item["target"], class_name="font-medium text-gray-900"),
                    class_name="text-sm",
                ),
                rx.el.p(item["time"], class_name="text-xs text-gray-400 mt-0.5"),
                class_name="ml-4 flex-1",
            ),
            rx.el.button(
                rx.icon(
                    "chevron-right",
                    size=16,
                    class_name="text-gray-400 hover:text-gray-600",
                ),
                class_name="p-1 rounded-md hover:bg-gray-50 transition-colors",
            ),
            class_name="flex items-center p-4 hover:bg-gray-50 transition-colors rounded-lg -mx-2",
        ),
        class_name="border-b border-gray-50 last:border-0",
    )


def activity_feed() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Recent Activity", class_name="text-lg font-semibold text-gray-900"
            ),
            rx.el.button(
                "View All",
                class_name="text-sm font-medium text-teal-600 hover:text-teal-700 transition-colors",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.div(
            rx.foreach(DashboardState.recent_activity, activity_item),
            class_name="flex flex-col",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm h-full",
    )