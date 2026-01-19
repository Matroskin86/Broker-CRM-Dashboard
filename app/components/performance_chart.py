import reflex as rx
from app.states.dashboard_state import DashboardState


def performance_chart() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Performance Overview",
                    class_name="text-lg font-semibold text-gray-900",
                ),
                rx.el.select(
                    rx.el.option("Last 6 Months"),
                    rx.el.option("This Year"),
                    rx.el.option("All Time"),
                    class_name="text-sm border-none bg-transparent text-gray-500 font-medium focus:ring-0 cursor-pointer",
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.el.div(
                rx.recharts.area_chart(
                    rx.recharts.cartesian_grid(
                        stroke_dasharray="3 3", vertical=False, stroke="#E5E7EB"
                    ),
                    rx.recharts.graphing_tooltip(
                        content_style={
                            "backgroundColor": "#fff",
                            "borderRadius": "8px",
                            "border": "1px solid #e5e7eb",
                            "boxShadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
                        },
                        item_style={"color": "#374151", "fontSize": "12px"},
                        label_style={
                            "color": "#111827",
                            "fontWeight": "600",
                            "marginBottom": "4px",
                        },
                        cursor={
                            "stroke": "#9ca3af",
                            "strokeWidth": 1,
                            "strokeDasharray": "3 3",
                        },
                    ),
                    rx.el.defs(
                        rx.el.linear_gradient(
                            rx.el.stop(
                                offset="5%", stop_color="#0d9488", stop_opacity=0.3
                            ),
                            rx.el.stop(
                                offset="95%", stop_color="#0d9488", stop_opacity=0
                            ),
                            id="tealGradient",
                            x1="0",
                            y1="0",
                            x2="0",
                            y2="1",
                        ),
                        rx.el.linear_gradient(
                            rx.el.stop(
                                offset="5%", stop_color="#10b981", stop_opacity=0.3
                            ),
                            rx.el.stop(
                                offset="95%", stop_color="#10b981", stop_opacity=0
                            ),
                            id="emeraldGradient",
                            x1="0",
                            y1="0",
                            x2="0",
                            y2="1",
                        ),
                    ),
                    rx.recharts.x_axis(
                        data_key="name",
                        axis_line=False,
                        tick_line=False,
                        tick={"fill": "#6B7280", "fontSize": 12},
                        dy=10,
                    ),
                    rx.recharts.y_axis(
                        axis_line=False,
                        tick_line=False,
                        tick={"fill": "#6B7280", "fontSize": 12},
                        dx=-10,
                    ),
                    rx.recharts.area(
                        type_="monotone",
                        data_key="deals",
                        stroke="#0d9488",
                        fill="url(#tealGradient)",
                        stroke_width=2,
                        name="Deals",
                    ),
                    rx.recharts.area(
                        type_="monotone",
                        data_key="revenue",
                        stroke="#10b981",
                        fill="url(#emeraldGradient)",
                        stroke_width=2,
                        name="Revenue",
                    ),
                    data=DashboardState.chart_data,
                    height=300,
                    width="100%",
                ),
                class_name="h-[300px] w-full",
            ),
            class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm h-full",
        ),
        class_name="w-full",
    )