import reflex as rx
from app.states.reminder_state import ReminderState, Reminder
from app.components.reminder_modal import reminder_modal


def reminder_status_badge(status: str) -> rx.Component:
    return rx.match(
        status,
        (
            "Pending",
            rx.el.span(
                "Pending",
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-amber-100 text-amber-800",
            ),
        ),
        (
            "Sent",
            rx.el.span(
                "Sent",
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800",
            ),
        ),
        (
            "Completed",
            rx.el.span(
                "Completed",
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800",
            ),
        ),
        rx.el.span(status),
    )


def reminder_type_icon(type: str) -> rx.Component:
    return rx.match(
        type,
        ("Call", rx.icon("phone", size=16, class_name="text-gray-400 mr-2")),
        ("Email", rx.icon("mail", size=16, class_name="text-gray-400 mr-2")),
        ("Meeting", rx.icon("users", size=16, class_name="text-gray-400 mr-2")),
        rx.icon("bell", size=16, class_name="text-gray-400 mr-2"),
    )


def reminder_row(reminder: Reminder) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    reminder["client_name"], class_name="font-medium text-gray-900"
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                reminder_type_icon(reminder["type"]),
                rx.el.span(reminder["message"], class_name="truncate max-w-xs"),
                class_name="flex items-center text-sm text-gray-500",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            reminder["scheduled_date"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            reminder_status_badge(reminder["status"]),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                rx.cond(
                    reminder["status"] == "Pending",
                    rx.el.button(
                        rx.icon(
                            "check",
                            size=18,
                            class_name="text-gray-400 hover:text-emerald-600",
                        ),
                        on_click=lambda: ReminderState.mark_as_completed(
                            reminder["id"]
                        ),
                        class_name="p-1 rounded hover:bg-gray-100",
                        title="Mark as Completed",
                    ),
                ),
                rx.cond(
                    reminder["status"] == "Pending",
                    rx.el.button(
                        rx.icon(
                            "send",
                            size=18,
                            class_name="text-gray-400 hover:text-blue-600",
                        ),
                        on_click=lambda: ReminderState.mark_as_sent(reminder["id"]),
                        class_name="p-1 rounded hover:bg-gray-100",
                        title="Mark as Sent",
                    ),
                ),
                rx.el.button(
                    rx.icon(
                        "pencil",
                        size=18,
                        class_name="text-gray-400 hover:text-teal-600",
                    ),
                    on_click=lambda: ReminderState.open_edit_modal(reminder),
                    class_name="p-1 rounded hover:bg-gray-100",
                    title="Edit",
                ),
                rx.el.button(
                    rx.icon(
                        "trash-2",
                        size=18,
                        class_name="text-gray-400 hover:text-red-600",
                    ),
                    on_click=lambda: ReminderState.delete_reminder(reminder["id"]),
                    class_name="p-1 rounded hover:bg-gray-100",
                    title="Delete",
                ),
                class_name="flex space-x-2 justify-end",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
        class_name="hover:bg-gray-50 transition-colors",
    )


def reminders_page() -> rx.Component:
    return rx.el.div(
        reminder_modal(),
        rx.el.div(
            rx.el.div(
                rx.el.h2("Reminders", class_name="text-xl font-bold text-gray-900"),
                rx.el.p(
                    "Stay on top of your client communications.",
                    class_name="text-sm text-gray-500 mt-1",
                ),
                class_name="flex flex-col",
            ),
            rx.el.button(
                rx.icon("plus", size=20, class_name="mr-2"),
                "Schedule Reminder",
                on_click=ReminderState.open_add_modal,
                class_name="flex items-center px-4 py-2 bg-teal-600 text-white rounded-lg hover:bg-teal-700 transition-colors shadow-sm text-sm font-medium",
            ),
            class_name="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6",
        ),
        rx.cond(
            ReminderState.reminders.length() > 0,
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Client",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Message",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Date",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Status",
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
                        rx.foreach(ReminderState.reminders, reminder_row),
                        class_name="bg-white divide-y divide-gray-200",
                    ),
                    class_name="min-w-full divide-y divide-gray-200",
                ),
                class_name="overflow-x-auto rounded-xl border border-gray-200 shadow-sm bg-white",
            ),
            rx.el.div(
                rx.icon("bell-off", size=48, class_name="text-gray-300 mb-4"),
                rx.el.h3(
                    "No reminders scheduled",
                    class_name="text-lg font-medium text-gray-900",
                ),
                rx.el.p(
                    "You're all caught up! Schedule a new reminder to get started.",
                    class_name="text-gray-500 mt-1",
                ),
                class_name="flex flex-col items-center justify-center p-12 bg-white rounded-xl border border-gray-200 mt-4 text-center",
            ),
        ),
        class_name="w-full animate-in fade-in duration-500",
    )