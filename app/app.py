import reflex as rx
from app.components.sidebar import sidebar
from app.components.header import header
from app.components.kpi_cards import kpi_grid
from app.components.activity_feed import activity_feed
from app.components.performance_chart import performance_chart
from app.components.client_distribution_chart import client_distribution_chart
from app.components.goals_tracker import goals_tracker
from app.components.clients_table import clients_table
from app.components.client_modal import client_modal
from app.components.reminders_page import reminders_page
from app.components.reminder_modal import reminder_modal
from app.states.dashboard_state import DashboardState


def dashboard_content() -> rx.Component:
    """The main content for the Dashboard tab."""
    return rx.el.div(
        kpi_grid(),
        rx.el.div(
            client_distribution_chart(),
            goals_tracker(),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6",
        ),
        rx.el.div(
            rx.el.div(performance_chart(), class_name="lg:col-span-2"),
            rx.el.div(activity_feed(), class_name="lg:col-span-1"),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
        ),
        class_name="w-full animate-in fade-in duration-500",
    )


def clients_content() -> rx.Component:
    """Content for Clients tab."""
    return rx.el.div(
        clients_table(),
        client_modal(),
        reminder_modal(),
        class_name="w-full animate-in fade-in duration-500",
    )


def reminders_content() -> rx.Component:
    """Content for Reminders tab."""
    return reminders_page()


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            rx.el.main(
                rx.el.div(
                    rx.cond(
                        DashboardState.active_tab == "Dashboard",
                        dashboard_content(),
                        rx.cond(
                            DashboardState.active_tab == "Clients",
                            clients_content(),
                            reminders_content(),
                        ),
                    ),
                    class_name="max-w-7xl mx-auto",
                ),
                class_name="flex-1 overflow-y-auto bg-gray-50 p-6 md:p-8",
            ),
            class_name="flex-1 flex flex-col min-w-0 h-screen transition-all duration-300 md:ml-64",
        ),
        class_name="flex h-screen bg-gray-50 font-['Inter']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        )
    ],
)
app.add_page(index, route="/")