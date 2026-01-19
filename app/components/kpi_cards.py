import reflex as rx
from app.states.dashboard_state import DashboardState, KPIItem


def kpi_card(item: KPIItem) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    item["title"], class_name="text-sm font-medium text-gray-500"
                ),
                rx.el.span(
                    rx.icon(item["icon"], size=18, class_name="text-gray-400"),
                    class_name="p-2 bg-gray-50 rounded-lg",
                ),
                class_name="flex justify-between items-start",
            ),
            rx.el.div(
                rx.el.div(
                    item["value"], class_name="text-2xl font-bold text-gray-900 mt-2"
                ),
                rx.el.div(
                    rx.cond(
                        item["trend"] == "up",
                        rx.icon("trending-up", size=14, class_name="mr-1"),
                        rx.icon("trending-down", size=14, class_name="mr-1"),
                    ),
                    rx.el.span(item["change"], class_name="font-medium"),
                    rx.el.span(" from last month", class_name="text-gray-400 ml-1"),
                    class_name=rx.cond(
                        item["trend"] == "up",
                        "flex items-center text-xs mt-1 text-emerald-600",
                        "flex items-center text-xs mt-1 text-red-600",
                    ),
                ),
            ),
            class_name="flex flex-col",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow duration-200",
    )


def kpi_grid() -> rx.Component:
    return rx.el.div(
        rx.foreach(DashboardState.kpi_stats, kpi_card),
        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
    )