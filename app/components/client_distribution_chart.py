import reflex as rx
from app.states.dashboard_state import DashboardState


def distribution_legend_item(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(class_name="w-3 h-3 rounded-full mr-2", bg=item["fill"]),
            rx.el.span(item["name"], class_name="text-sm text-gray-600"),
            class_name="flex items-center",
        ),
        rx.el.span(item["value"], class_name="text-sm font-semibold text-gray-900"),
        class_name="flex items-center justify-between mb-2 last:mb-0",
    )


def client_distribution_chart() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Client Distribution", class_name="text-lg font-semibold text-gray-900"
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("All Clients", value="All"),
                    rx.el.option("Active", value="Active"),
                    rx.el.option("Pending", value="Pending"),
                    rx.el.option("Closed", value="Closed"),
                    rx.el.option("Lost", value="Lost"),
                    value=DashboardState.distribution_filter,
                    on_change=DashboardState.set_distribution_filter,
                    class_name="text-sm border-0 bg-transparent text-gray-500 font-medium focus:ring-0 cursor-pointer p-0 pr-8 text-right hover:text-gray-700 transition-colors",
                ),
                class_name="relative",
            ),
            class_name="flex items-center justify-between mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.recharts.pie_chart(
                    rx.recharts.pie(
                        rx.foreach(
                            DashboardState.filtered_client_distribution,
                            lambda entry: rx.recharts.cell(fill=entry["fill"]),
                        ),
                        data=DashboardState.filtered_client_distribution,
                        data_key="value",
                        name_key="name",
                        cx="50%",
                        cy="50%",
                        inner_radius="60%",
                        outer_radius="80%",
                        padding_angle=2,
                        stroke="none",
                        stroke_width=0,
                    ),
                    height="100%",
                    width="100%",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            DashboardState.total_clients_metric,
                            class_name="text-2xl font-bold text-gray-900 block leading-none",
                        ),
                        rx.el.span(
                            "Clients", class_name="text-xs text-gray-500 font-medium"
                        ),
                        class_name="text-center",
                    ),
                    class_name="absolute inset-0 flex items-center justify-center pointer-events-none",
                ),
                class_name="relative h-48 w-48 mx-auto",
            ),
            rx.el.div(
                rx.foreach(
                    DashboardState.filtered_client_distribution,
                    distribution_legend_item,
                ),
                class_name="flex-1 mt-6 lg:mt-0 lg:ml-8",
            ),
            class_name="flex flex-col lg:flex-row items-center justify-center",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm h-full",
    )