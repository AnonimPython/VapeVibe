import reflex as rx

config = rx.Config(
    app_name="VapeVibe",
    frontend_port=3000,
    db_url="postgresql://postgres:12345@localhost:5432/vapevibe",
    env=rx.Env.DEV,
)