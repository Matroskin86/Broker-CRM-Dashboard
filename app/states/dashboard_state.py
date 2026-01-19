import reflex as rx
from typing import TypedDict
import random


class KPIItem(TypedDict):
    title: str
    value: str
    change: str
    trend: str
    icon: str


class ActivityItem(TypedDict):
    name: str
    action: str
    target: str
    time: str
    avatar_seed: str


class ChartItem(TypedDict):
    name: str
    deals: int
    revenue: int


class ClientDistributionItem(TypedDict):
    name: str
    value: int
    fill: str


class GoalItem(TypedDict):
    title: str
    current: int
    target: int
    unit: str
    color: str


class DashboardState(rx.State):
    """State management for the dashboard."""

    nav_items: list[str] = ["Dashboard", "Clients", "Reminders"]
    active_tab: str = "Dashboard"
    search_query: str = ""
    is_profile_open: bool = False
    distribution_filter: str = "All"
    client_distribution: list[ClientDistributionItem] = [
        {"name": "Active", "value": 850, "fill": "#0d9488"},
        {"name": "Pending", "value": 234, "fill": "#f59e0b"},
        {"name": "Closed", "value": 120, "fill": "#3b82f6"},
        {"name": "Lost", "value": 30, "fill": "#ef4444"},
    ]
    goals: list[GoalItem] = [
        {
            "title": "New Clients",
            "current": 45,
            "target": 60,
            "unit": "",
            "color": "teal",
        },
        {
            "title": "Deals Closed",
            "current": 28,
            "target": 40,
            "unit": "",
            "color": "emerald",
        },
        {
            "title": "Revenue Target",
            "current": 850,
            "target": 1200,
            "unit": "$k",
            "color": "blue",
        },
    ]

    @rx.var
    def filtered_client_distribution(self) -> list[ClientDistributionItem]:
        """Filter the distribution data based on selection."""
        if self.distribution_filter == "All":
            return self.client_distribution
        return [
            item
            for item in self.client_distribution
            if item["name"] == self.distribution_filter
        ]

    @rx.var
    def total_clients_metric(self) -> str:
        """Calculate total clients based on the filtered view."""
        data = self.client_distribution
        if self.distribution_filter != "All":
            data = [
                item
                for item in self.client_distribution
                if item["name"] == self.distribution_filter
            ]
        total = sum([item["value"] for item in data])
        return f"{total:,}"

    kpi_stats: list[KPIItem] = [
        {
            "title": "Total Clients",
            "value": "1,234",
            "change": "+12%",
            "trend": "up",
            "icon": "users",
        },
        {
            "title": "Active Deals",
            "value": "45",
            "change": "+5%",
            "trend": "up",
            "icon": "briefcase",
        },
        {
            "title": "Revenue",
            "value": "$1.2M",
            "change": "+8%",
            "trend": "up",
            "icon": "dollar-sign",
        },
        {
            "title": "Conversion Rate",
            "value": "24%",
            "change": "-2%",
            "trend": "down",
            "icon": "percent",
        },
    ]
    recent_activity: list[ActivityItem] = [
        {
            "name": "Sarah Chen",
            "action": "updated deal status for",
            "target": "TechFlow Systems",
            "time": "2 mins ago",
            "avatar_seed": "sarah",
        },
        {
            "name": "Mike Ross",
            "action": "added a new note to",
            "target": "Pearson Legal",
            "time": "15 mins ago",
            "avatar_seed": "mike",
        },
        {
            "name": "Jessica Pearson",
            "action": "scheduled a meeting with",
            "target": "Global Dynamics",
            "time": "1 hour ago",
            "avatar_seed": "jessica",
        },
        {
            "name": "Harvey Specter",
            "action": "closed deal with",
            "target": "Hardman Group",
            "time": "3 hours ago",
            "avatar_seed": "harvey",
        },
        {
            "name": "Louis Litt",
            "action": "sent contract to",
            "target": "Velcro Corp",
            "time": "5 hours ago",
            "avatar_seed": "louis",
        },
    ]
    chart_data: list[ChartItem] = [
        {"name": "Jan", "deals": 65, "revenue": 4000},
        {"name": "Feb", "deals": 59, "revenue": 3000},
        {"name": "Mar", "deals": 80, "revenue": 2000},
        {"name": "Apr", "deals": 81, "revenue": 2780},
        {"name": "May", "deals": 56, "revenue": 1890},
        {"name": "Jun", "deals": 55, "revenue": 2390},
        {"name": "Jul", "deals": 40, "revenue": 3490},
    ]

    @rx.event
    def set_active_tab(self, tab: str):
        self.active_tab = tab

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def toggle_profile(self):
        self.is_profile_open = not self.is_profile_open

    @rx.event
    def set_distribution_filter(self, value: str):
        self.distribution_filter = value

    @rx.event
    def nav_link_classes(self, item: str) -> str:
        pass