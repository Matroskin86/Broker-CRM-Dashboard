import reflex as rx
from app.states.dashboard_state import DashboardState


def goal_item(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(item["title"], class_name="text-sm font-medium text-gray-700"),
            rx.el.span(
                rx.el.span(item["current"], class_name="font-semibold text-gray-900"),
                rx.el.span(
                    item["unit"], class_name="text-gray-500 ml-0.5 text-xs font-medium"
                ),
                rx.el.span(" / ", class_name="text-gray-400 mx-1"),
                rx.el.span(item["target"], class_name="text-gray-500"),
                rx.el.span(
                    item["unit"], class_name="text-gray-500 ml-0.5 text-xs font-medium"
                ),
                class_name="text-sm",
            ),
            class_name="flex justify-between items-center mb-2",
        ),
        rx.el.div(
            rx.el.div(
                class_name=rx.match(
                    item["color"],
                    (
                        "teal",
                        "h-2 rounded-full bg-teal-500 transition-all duration-500",
                    ),
                    (
                        "emerald",
                        "h-2 rounded-full bg-emerald-500 transition-all duration-500",
                    ),
                    (
                        "blue",
                        "h-2 rounded-full bg-blue-500 transition-all duration-500",
                    ),
                    "h-2 rounded-full bg-gray-500 transition-all duration-500",
                ),
                style={
                    "width": (item["current"] / item["target"] * 100).to_string() + "%"
                },
            ),
            class_name="w-full bg-gray-100 rounded-full h-2 overflow-hidden",
        ),
        class_name="mb-5 last:mb-0",
    )


def goals_tracker() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3("Monthly Goals", class_name="text-lg font-semibold text-gray-900"),
            rx.el.button(
                "Edit Goals",
                class_name="text-sm font-medium text-teal-600 hover:text-teal-700 transition-colors",
            ),
            class_name="flex items-center justify-between mb-6",
        ),
        rx.el.div(
            rx.foreach(DashboardState.goals, goal_item), class_name="flex flex-col"
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm h-full",
    )