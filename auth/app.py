"""Backend de acceso a /docs/ para la landing de Contalibra -- config sobre
libra_web_kit.docs_auth (extraído 2026-07-26, ver
wiki/analyses/auditoria-duplicacion-familia-libra.md)."""
from libra_web_kit.docs_auth import build_docs_login_app, DocsLoginTheme

app = build_docs_login_app(
    product_name="Contalibra",
    apex_domain_default="contalibra.com.ar",
    secret_key_env="SECRET_KEY",
    secret_key_default="contalibra-docs-secret-change-me",
    verify_path="/api/auth/verify",
    slug_placeholder="tu-empresa",
    theme=DocsLoginTheme(accent="#2563eb", accent_hover="#1d4ed8"),
)
