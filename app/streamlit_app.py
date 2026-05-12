# Imports
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import streamlit.components.v1 as components
import story_content as story

# Define project file paths
ROOT = Path(__file__).resolve().parents[1]
APP_DIR = Path(__file__).resolve().parent
PROCESSED = ROOT / "data" / "processed"
MAIN_PATH = PROCESSED / "main_yearly.csv"
OPTIONAL_PATH = PROCESSED / "optional_yearly.csv"
STYLES_PATH = APP_DIR / "styles.css"


# Configure the Streamlit page
st.set_page_config(
    page_title=story.PAGE_TITLE,
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded",
)


# Detect the current Streamlit theme
def current_theme_is_dark() -> bool:
    theme_values = []
    try:
        theme_values.append(st.get_option("theme.base"))
    except Exception:
        pass

    try:
        theme = st.context.theme or {}
        for key in ("type", "base"):
            value = theme.get(key) if hasattr(theme, "get") else getattr(theme, key, None)
            theme_values.append(value)
    except Exception:
        pass

    return any(str(value).lower() == "dark" for value in theme_values if value)


# Add the day mode toggle
sys_dark = current_theme_is_dark()
with st.sidebar:
    st.markdown(story.DISPLAY["heading"])
    day_mode = st.toggle(
        story.DISPLAY["day_mode"],
        value=not sys_dark,
        help=story.DISPLAY["day_help"],
    )


# Set page colors based on theme
dark = not day_mode
PAGE_TEXT_COLOR = "#f9fafb" if dark else "#111827"
PAGE_MUTED_TEXT_COLOR = "#cbd5e1" if dark else "#64748b"
PAGE_BG_COLOR = "#0e1117" if dark else "#f6f7fb"
PAGE_SECONDARY_BG_COLOR = "#262730" if dark else "#eef2f7"
PAGE_CARD_BG_COLOR = "rgba(17, 24, 39, 0.74)" if dark else "#ffffff"
PAGE_PANEL_BG_COLOR = "rgba(31, 41, 55, 0.48)" if dark else "#f8fafc"
PAGE_BORDER_COLOR = (
    "rgba(148, 163, 184, 0.32)"
    if dark
    else "rgba(15, 23, 42, 0.12)"
)
PAGE_PRIMARY_COLOR = "#60a5fa" if dark else "#2563eb"
PAGE_ACCENT_COLOR = "#2dd4bf" if dark else "#0f766e"
PAGE_WARNING_COLOR = "#fbbf24" if dark else "#b45309"
PAGE_CAUTION_BG_COLOR = (
    "rgba(251, 191, 36, 0.14)" if dark else "#fffbeb"
)
PAGE_LINK_COLOR = "#38bdf8" if dark else "#2563eb"


# Load custom CSS into the app
def load_css() -> None:
    css = STYLES_PATH.read_text(encoding="utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            --text-color: {PAGE_TEXT_COLOR};
            --muted-text-color: {PAGE_MUTED_TEXT_COLOR};
            --background-color: {PAGE_BG_COLOR};
            --secondary-background-color: {PAGE_SECONDARY_BG_COLOR};
            --card-background-color: {PAGE_CARD_BG_COLOR};
            --panel-background-color: {PAGE_PANEL_BG_COLOR};
            --border-color: {PAGE_BORDER_COLOR};
            --primary-color: {PAGE_PRIMARY_COLOR};
            --accent-color: {PAGE_ACCENT_COLOR};
            --warning-color: {PAGE_WARNING_COLOR};
            --caution-background-color: {PAGE_CAUTION_BG_COLOR};
            --link-color: {PAGE_LINK_COLOR};
        }}
        {css}
        </style>
        """,
        unsafe_allow_html=True,
    )

load_css()

# Inject the reading progress bar
def inject_reading_progress_bar() -> None:
    components.html(
        """
        <script>
        (() => {
            const doc = window.parent.document;
            let bar = doc.getElementById("reading-progress-bar");
            if (!bar) {
                bar = doc.createElement("div");
                bar.id = "reading-progress-bar";
                doc.body.appendChild(bar);
            }

            const scrollTarget = doc.querySelector('[data-testid="stMain"]') || window.parent;
            const update = () => {
                const isWindow = scrollTarget === window.parent;
                const root = doc.documentElement;
                const scrollTop = isWindow ? (window.parent.scrollY || root.scrollTop || 0) : scrollTarget.scrollTop;
                const scrollHeight = isWindow ? Math.max(root.scrollHeight, doc.body.scrollHeight) : scrollTarget.scrollHeight;
                const clientHeight = isWindow ? root.clientHeight : scrollTarget.clientHeight;
                const maxScroll = Math.max(scrollHeight - clientHeight, 1);
                const progress = Math.min(100, Math.max(0, (scrollTop / maxScroll) * 100));
                bar.style.width = `${progress}%`;
            };

            if (window.parent.__adulthoodProgressUpdate) {
                const oldTarget = window.parent.__adulthoodProgressTarget || window.parent;
                oldTarget.removeEventListener("scroll", window.parent.__adulthoodProgressUpdate);
                window.parent.removeEventListener("resize", window.parent.__adulthoodProgressUpdate);
            }
            window.parent.__adulthoodProgressUpdate = update;
            window.parent.__adulthoodProgressTarget = scrollTarget;
            scrollTarget.addEventListener("scroll", update, { passive: true });
            window.parent.addEventListener("resize", update);
            update();
        })();
        </script>
        """,
        height=0,
        width=0,
    )


inject_reading_progress_bar()


# Enable smooth sidebar navigation
def inject_smooth_anchor_navigation() -> None:
    components.html(
        """
        <script>
        (() => {
            const doc = window.parent.document;
            const reducedMotion = window.parent.matchMedia("(prefers-reduced-motion: reduce)");

            if (window.parent.__adulthoodNavClick) {
                doc.removeEventListener("click", window.parent.__adulthoodNavClick);
            }

            window.parent.__adulthoodNavClick = (event) => {
                const link = event.target.closest('.story-nav a[href^="#"]');
                if (!link) {
                    return;
                }

                const target = doc.querySelector(link.getAttribute("href"));
                if (!target) {
                    return;
                }

                event.preventDefault();
                target.scrollIntoView({
                    behavior: reducedMotion.matches ? "auto" : "smooth",
                    block: "start",
                });
                window.parent.history.replaceState(null, "", link.getAttribute("href"));
            };

            doc.addEventListener("click", window.parent.__adulthoodNavClick);
        })();
        </script>
        """,
        height=0,
        width=0,
    )

# Animate the hero background particles
def inject_hero_particles() -> None:
    components.html(
        """
        <script>
        (() => {
            const win = window.parent;
            const doc = win.document;
            const startedAt = Date.now();
            const reducedMotion = win.matchMedia("(prefers-reduced-motion: reduce)").matches;
            const particleCount = 42;
            const maxDistance = 118;

            const hexToRgb = (value) => {
                const hex = value.trim().replace("#", "");
                const full = hex.length === 3
                    ? hex.split("").map((char) => char + char).join("")
                    : hex;
                const numeric = Number.parseInt(full, 16);
                if (Number.isNaN(numeric)) {
                    return { r: 96, g: 165, b: 250 };
                }
                return {
                    r: (numeric >> 16) & 255,
                    g: (numeric >> 8) & 255,
                    b: numeric & 255,
                };
            };

            const cssVar = (name, fallback) => {
                const value = win.getComputedStyle(doc.querySelector(".stApp") || doc.documentElement)
                    .getPropertyValue(name)
                    .trim();
                return value || fallback;
            };

            const primary = hexToRgb(cssVar("--primary-color", "#60a5fa"));
            const accent = hexToRgb(cssVar("--accent-color", "#2dd4bf"));

            const startParticles = () => {
                const canvas = doc.querySelector(".hero-particle-canvas");
                const rect = canvas ? canvas.getBoundingClientRect() : { width: 0, height: 0 };
                if (!canvas || rect.width < 20 || rect.height < 20) {
                    if (Date.now() - startedAt < 5000) {
                        win.requestAnimationFrame(startParticles);
                    }
                    return;
                }

                const ctx = canvas.getContext("2d");
                let particles = [];

                const resize = () => {
                    const ratio = win.devicePixelRatio || 1;
                    const nextRect = canvas.getBoundingClientRect();
                    canvas.width = Math.max(1, Math.floor(nextRect.width * ratio));
                    canvas.height = Math.max(1, Math.floor(nextRect.height * ratio));
                    ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

                    particles = Array.from({ length: particleCount }, () => ({
                        x: Math.random() * nextRect.width,
                        y: Math.random() * nextRect.height,
                        vx: (Math.random() - 0.5) * 0.16,
                        vy: (Math.random() - 0.5) * 0.16,
                        radius: 1.1 + Math.random() * 1.2,
                    }));
                };

                const draw = () => {
                    const nextRect = canvas.getBoundingClientRect();
                    ctx.clearRect(0, 0, nextRect.width, nextRect.height);

                    for (let i = 0; i < particles.length; i += 1) {
                        const p = particles[i];
                        if (!reducedMotion) {
                            p.x += p.vx;
                            p.y += p.vy;
                            if (p.x < 0 || p.x > nextRect.width) p.vx *= -1;
                            if (p.y < 0 || p.y > nextRect.height) p.vy *= -1;
                        }

                        for (let j = i + 1; j < particles.length; j += 1) {
                            const q = particles[j];
                            const dx = p.x - q.x;
                            const dy = p.y - q.y;
                            const distance = Math.sqrt(dx * dx + dy * dy);
                            if (distance < maxDistance) {
                                const alpha = (1 - distance / maxDistance) * 0.14;
                                ctx.strokeStyle = `rgba(${primary.r}, ${primary.g}, ${primary.b}, ${alpha})`;
                                ctx.lineWidth = 0.7;
                                ctx.beginPath();
                                ctx.moveTo(p.x, p.y);
                                ctx.lineTo(q.x, q.y);
                                ctx.stroke();
                            }
                        }

                        const dotAlpha = 0.18 + (i % 5) * 0.015;
                        ctx.fillStyle = `rgba(${accent.r}, ${accent.g}, ${accent.b}, ${dotAlpha})`;
                        ctx.beginPath();
                        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                        ctx.fill();
                    }

                    if (!reducedMotion) {
                        win.__adulthoodParticleFrame = win.requestAnimationFrame(draw);
                    }
                };

                if (win.__adulthoodParticleFrame) {
                    win.cancelAnimationFrame(win.__adulthoodParticleFrame);
                }
                if (win.__adulthoodParticleResize) {
                    win.removeEventListener("resize", win.__adulthoodParticleResize);
                }

                win.__adulthoodParticleResize = () => {
                    resize();
                    draw();
                };
                win.addEventListener("resize", win.__adulthoodParticleResize);

                resize();
                draw();
            };

            startParticles();
        })();
        </script>
        """,
        height=0,
        width=0,
    )

# Set Plotly chart colors
PLOT_TEXT_COLOR = PAGE_TEXT_COLOR
PLOT_MUTED_TEXT_COLOR = PAGE_MUTED_TEXT_COLOR
PLOT_GRID_COLOR = "rgba(148, 163, 184, 0.28)" if dark else "#e2e8f0"
PLOT_AXIS_COLOR = "rgba(148, 163, 184, 0.65)" if dark else "#cbd5e1"
PLOT_BG_COLOR = "rgba(0,0,0,0)"
PLOT_TEMPLATE = "plotly_dark" if dark else "plotly_white"
PLOT_HOVER_BG_COLOR = "#111827" if dark else "#ffffff"
SERIES_COLORS = {
    "blue": "#60a5fa" if dark else "#2563eb",
    "coral": "#fb7185" if dark else "#dc2626",
    "teal": "#2dd4bf" if dark else "#0f766e",
    "amber": "#fbbf24" if dark else "#b45309",
}
PLOTLY_CHART_CONFIG = {"displayModeBar": False}

# Load processed data files
@st.cache_data
def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    if not MAIN_PATH.exists():
        raise FileNotFoundError(f"Missing processed file: {MAIN_PATH}")
    main_df = pd.read_csv(MAIN_PATH)
    optional_df = (
        pd.read_csv(OPTIONAL_PATH) if OPTIONAL_PATH.exists() else pd.DataFrame()
    )
    main_df["year"] = main_df["year"].astype(int)
    if not optional_df.empty:
        optional_df["year"] = optional_df["year"].astype(int)
    return main_df, optional_df

# Check that required columns exist
def require_columns(df: pd.DataFrame, columns: list[str]) -> None:
    missing = [col for col in columns if col not in df.columns]
    if missing:
        st.error(
            "Missing required columns in data/processed/main_yearly.csv: "
            + ", ".join(missing)
        )
        st.stop()

# Apply shared chart layout settings
def chart_layout(fig: go.Figure, title: str, y_title: str | None = None) -> go.Figure:
    fig.update_layout(
        title={
            "text": title,
            "x": 0,
            "xanchor": "left",
            "font": {"color": PLOT_TEXT_COLOR},
        },
        height=470,
        margin={"l": 20, "r": 20, "t": 72, "b": 45},
        template=PLOT_TEMPLATE,
        paper_bgcolor=PLOT_BG_COLOR,
        plot_bgcolor=PLOT_BG_COLOR,
        hovermode="x unified",
        hoverlabel={
            "bgcolor": PLOT_HOVER_BG_COLOR,
            "bordercolor": PLOT_AXIS_COLOR,
            "font": {"color": PLOT_TEXT_COLOR},
        },
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "left",
            "x": 0,
            "font": {"color": PLOT_TEXT_COLOR},
        },
        font={"family": "Arial, sans-serif", "color": PLOT_TEXT_COLOR},
    )
    fig.update_xaxes(
        title_text=story.AXIS["year"],
        showgrid=False,
        zeroline=False,
        ticks="outside",
        tickcolor=PLOT_AXIS_COLOR,
        tickfont={"color": PLOT_MUTED_TEXT_COLOR},
        title_font={"color": PLOT_TEXT_COLOR},
        linecolor=PLOT_AXIS_COLOR,
    )
    fig.update_yaxes(
        title_text=y_title,
        gridcolor=PLOT_GRID_COLOR,
        zeroline=False,
        ticks="outside",
        tickcolor=PLOT_AXIS_COLOR,
        tickfont={"color": PLOT_MUTED_TEXT_COLOR},
        title_font={"color": PLOT_TEXT_COLOR},
        linecolor=PLOT_AXIS_COLOR,
    )
    return fig

# Display a Plotly chart
def show_plotly_chart(fig: go.Figure) -> None:
    st.plotly_chart(
        fig,
        use_container_width=True,
        config=PLOTLY_CHART_CONFIG,
        theme=None,
    )

# Add one line series to a chart
def add_line(
    fig: go.Figure,
    df: pd.DataFrame,
    column: str,
    name: str,
    color: str,
    row: int | None = None,
    col: int | None = None,
    dash: str | None = None,
) -> None:
    plot_df = df.loc[df[column].notna(), ["year", column]]
    fig.add_trace(
        go.Scatter(
            x=plot_df["year"],
            y=plot_df[column],
            mode="lines",
            name=name,
            line={"color": color, "width": 2.8, "dash": dash or "solid"},
            hovertemplate="%{x}<br>" + name + ": %{y:,.2f}<extra></extra>",
        ),
        row=row,
        col=col,
    )

# Add an HTML anchor for navigation
def anchor(section_id: str) -> None:
    st.markdown(
        f'<span class="anchor" id="{section_id}"></span>', unsafe_allow_html=True
    )

# Render a chart caption
def caption(text: str) -> None:
    st.markdown(f'<div class="caption">{text}</div>', unsafe_allow_html=True)

# Render a caution note
def caution(text: str) -> None:
    st.markdown(
        f'<div class="caution"><div class="caution-label">{story.DISPLAY["caution_label"]}</div><div>{text}</div></div>',
        unsafe_allow_html=True,
    )

# Render the chart reading tip
def look_for(text: str) -> None:
    st.markdown(f'<div class="look-for">{text}</div>', unsafe_allow_html=True)

# Render the chart hook text
def story_hook(text: str) -> None:
    st.markdown(f'<div class="story-hook">{text}</div>', unsafe_allow_html=True)

# Render a text section card
def section_card(title: str, body: str, kicker: str | None = None) -> None:
    with st.container(border=True):
        st.markdown('<div class="section-card-marker"></div>', unsafe_allow_html=True)
        if kicker:
            st.markdown(
                f'<div class="section-kicker">{kicker}</div>',
                unsafe_allow_html=True,
            )
        st.header(title)
        st.markdown(body)

# Render a visual chart card
def visual_card(
    fig: go.Figure,
    hook_text: str,
    tip: str,
    caption_text: str,
    caution_text: str,
) -> None:
    with st.container(border=True):
        st.markdown('<div class="visual-card-marker"></div>', unsafe_allow_html=True)
        story_hook(hook_text)
        look_for(tip)
        show_plotly_chart(fig)
        caption(caption_text)
        caution(caution_text)

# Build the sidebar navigation HTML
def sidebar_nav() -> str:
    links = "\n".join(
        f'          <a href="#{section_id}">{label}</a>'
        for section_id, label in story.NAV_ITEMS
    )
    return f"""
        <nav class="story-nav">
          <div class="nav-label">Contents</div>
{links}
          <p>{story.NAV_NOTE}</p>
        </nav>
        """

# Build the hero section HTML
def hero_html(hero_class: str) -> str:
    hero = story.HERO
    return f"""
    <section class="{hero_class}">
      <canvas class="hero-particle-canvas" aria-hidden="true"></canvas>
      <div class="hero-eyebrow">{hero["eyebrow"]}</div>
      <h1>{story.TITLE}</h1>
      <p class="hero-subtitle">{hero["subtitle"]}</p>
      <p class="hero-opening">{story.OPENING_SENTENCE}</p>
      <div class="hero-research-card">
        <h3>{hero["question_label"]}</h3>
        <p><strong>{hero["question"]}</strong></p>
        <h3>{hero["does_label"]}</h3>
        <p>{hero["does"]}</p>
        <h3>{hero["does_not_label"]}</h3>
        <p>{hero["does_not"]}</p>
      </div>
    </section>
    """

# Render one story section
def story_section(info: dict) -> None:
    anchor(info["anchor"])
    section_card(info["section_title"], info["section_body"], info["kicker"])

# Render one chart section
def chart_card(fig: go.Figure, info: dict) -> None:
    visual_card(fig, info["hook"], info["tip"], info["caption"], info["caution"])

# Build source label chips
def source_chips_html() -> str:
    parts = []
    for label, muted in story.DATA_SOURCES["chips"]:
        css_class = "source-chip source-chip-muted" if muted else "source-chip"
        parts.append(f'          <span class="{css_class}">{label}</span>')
    return '<div class="source-chips">\n' + "\n".join(parts) + "\n        </div>"

# Build source information boxes
def source_box_html(box: dict) -> str:
    items = "\n".join(f"          <li>{item}</li>" for item in box["items"])
    return f"""
        <div class="source-box">
        <strong>{box["title"]}</strong>
        <ul>
{items}
        </ul>
        </div>
        """

# Load data and stop if files are missing
try:
    main, optional = load_data()
except FileNotFoundError as exc:
    st.error(str(exc))
    st.info(story.DISPLAY["missing_data_hint"])
    st.stop()

# List columns needed for all charts
required_columns = [
    "year",
    "income_index",
    "wage_index",
    "home_price_to_family_income",
    "home_price_work_years",
    "medical_index",
    "medical_to_wage_index",
    "education_childcare_index",
    "education_childcare_to_wage_index",
    "median_age_first_marriage_men",
    "median_age_first_marriage_women",
]
require_columns(main, required_columns)

# Show the sidebar contents list
with st.sidebar:
    st.markdown(sidebar_nav(), unsafe_allow_html=True)

inject_smooth_anchor_navigation()

# Choose the hero animation state
hero_class = "hero"
if not st.session_state.get("hero_seen"):
    hero_class = "hero hero-animate"
    st.session_state.hero_seen = True

# Render the overview hero section
anchor("overview")
st.markdown(hero_html(hero_class), unsafe_allow_html=True)
inject_hero_particles()
section_card(story.OVERVIEW["title"], story.OVERVIEW["body"], story.OVERVIEW["kicker"])

# Render the wage baseline chart
wage = story.CHARTS["wage"]
story_section(wage)
fig1 = go.Figure()
add_line(
    fig1,
    main,
    "income_index",
    story.SERIES["income"],
    SERIES_COLORS["blue"],
)
add_line(
    fig1,
    main,
    "wage_index",
    story.SERIES["wage"],
    SERIES_COLORS["coral"],
)
fig1.add_vline(x=1964, line_width=1, line_dash="dash", line_color=PLOT_AXIS_COLOR)
fig1.add_annotation(
    x=1964,
    y=1.02,
    yref="paper",
    text=wage["wage_note"],
    showarrow=False,
    font={"size": 11, "color": PLOT_MUTED_TEXT_COLOR},
)
chart_layout(fig1, wage["chart_title"], wage["y_title"])
chart_card(fig1, wage)

# Render the housing burden chart
housing = story.CHARTS["housing"]
story_section(housing)
fig2 = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.12,
    subplot_titles=housing["subtitles"],
)
add_line(
    fig2,
    main,
    "home_price_to_family_income",
    story.SERIES["home_ratio"],
    SERIES_COLORS["amber"],
    row=1,
    col=1,
)
add_line(
    fig2,
    main,
    "home_price_work_years",
    story.SERIES["home_years"],
    SERIES_COLORS["teal"],
    row=2,
    col=1,
)
fig2.update_layout(
    title={
        "text": housing["chart_title"],
        "x": 0,
        "xanchor": "left",
        "font": {"color": PLOT_TEXT_COLOR},
    },
    height=580,
    margin={"l": 20, "r": 20, "t": 92, "b": 45},
    template=PLOT_TEMPLATE,
    paper_bgcolor=PLOT_BG_COLOR,
    plot_bgcolor=PLOT_BG_COLOR,
    hovermode="x unified",
    hoverlabel={
        "bgcolor": PLOT_HOVER_BG_COLOR,
        "bordercolor": PLOT_AXIS_COLOR,
        "font": {"color": PLOT_TEXT_COLOR},
    },
    legend={
        "orientation": "h",
        "yanchor": "bottom",
        "y": 1.04,
        "xanchor": "left",
        "x": 0,
        "font": {"color": PLOT_TEXT_COLOR},
    },
    font={"family": "Arial, sans-serif", "color": PLOT_TEXT_COLOR},
)
fig2.update_annotations(font={"color": PLOT_TEXT_COLOR})
fig2.update_xaxes(
    showgrid=False,
    zeroline=False,
    ticks="outside",
    tickcolor=PLOT_AXIS_COLOR,
    tickfont={"color": PLOT_MUTED_TEXT_COLOR},
    title_font={"color": PLOT_TEXT_COLOR},
    linecolor=PLOT_AXIS_COLOR,
)
fig2.update_xaxes(
    title_text=story.AXIS["year"],
    showgrid=False,
    zeroline=False,
    ticks="outside",
    tickcolor=PLOT_AXIS_COLOR,
    tickfont={"color": PLOT_MUTED_TEXT_COLOR},
    title_font={"color": PLOT_TEXT_COLOR},
    linecolor=PLOT_AXIS_COLOR,
    row=2,
    col=1,
)
fig2.update_yaxes(
    title_text=story.AXIS["ratio"],
    gridcolor=PLOT_GRID_COLOR,
    zeroline=False,
    ticks="outside",
    tickcolor=PLOT_AXIS_COLOR,
    tickfont={"color": PLOT_MUTED_TEXT_COLOR},
    title_font={"color": PLOT_TEXT_COLOR},
    linecolor=PLOT_AXIS_COLOR,
    row=1,
    col=1,
)
fig2.update_yaxes(
    title_text=story.AXIS["years"],
    gridcolor=PLOT_GRID_COLOR,
    zeroline=False,
    ticks="outside",
    tickcolor=PLOT_AXIS_COLOR,
    tickfont={"color": PLOT_MUTED_TEXT_COLOR},
    title_font={"color": PLOT_TEXT_COLOR},
    linecolor=PLOT_AXIS_COLOR,
    row=2,
    col=1,
)
chart_card(fig2, housing)

# Render the medical price chart
medical = story.CHARTS["medical"]
story_section(medical)

fig3 = go.Figure()
add_line(
    fig3,
    main,
    "medical_index",
    story.SERIES["medical"],
    SERIES_COLORS["teal"],
)
add_line(
    fig3,
    main,
    "medical_to_wage_index",
    story.SERIES["medical_wage"],
    SERIES_COLORS["coral"],
)
fig3.add_vline(x=1964, line_width=1, line_dash="dash", line_color=PLOT_AXIS_COLOR)
chart_layout(fig3, medical["chart_title"], medical["y_title"])
chart_card(fig3, medical)

# Render the education and childcare chart
education = story.CHARTS["education"]
story_section(education)

fig4 = go.Figure()
add_line(
    fig4,
    main,
    "education_childcare_index",
    story.SERIES["education"],
    SERIES_COLORS["amber"],
)
add_line(
    fig4,
    main,
    "education_childcare_to_wage_index",
    story.SERIES["education_wage"],
    SERIES_COLORS["coral"],
)
fig4.add_vline(x=1978, line_width=1, line_dash="dash", line_color=PLOT_AXIS_COLOR)
fig4.add_annotation(
    x=1978,
    y=1.02,
    yref="paper",
    text=education["series_note"],
    showarrow=False,
    font={"size": 11, "color": PLOT_MUTED_TEXT_COLOR},
)
chart_layout(fig4, education["chart_title"], education["y_title"])
chart_card(fig4, education)

# Render the marriage age chart
marriage = story.CHARTS["marriage"]
story_section(marriage)

fig5 = go.Figure()
add_line(
    fig5,
    main,
    "median_age_first_marriage_men",
    story.SERIES["men"],
    SERIES_COLORS["teal"],
)
add_line(
    fig5,
    main,
    "median_age_first_marriage_women",
    story.SERIES["women"],
    SERIES_COLORS["coral"],
)
chart_layout(fig5, marriage["chart_title"], marriage["y_title"])
chart_card(fig5, marriage)

# Render background notes
for note in story.BACKGROUND_EXPANDERS:
    with st.expander(note["title"]):
        st.markdown(note["body"])

# Render the methods section
anchor(story.METHODS["anchor"])
with st.expander(story.METHODS["title"], expanded=True):
    st.markdown(story.METHODS["body"])
    if not optional.empty:
        st.caption(story.METHODS["optional_caption"])

# Render the data sources section
anchor(story.DATA_SOURCES["anchor"])
with st.expander(story.DATA_SOURCES["title"], expanded=True):
    st.markdown(story.DATA_SOURCES["intro"])
    st.markdown(source_chips_html(), unsafe_allow_html=True)
    for box in story.DATA_SOURCES["boxes"]:
        st.markdown(source_box_html(box), unsafe_allow_html=True)

# Render the limitations section
anchor(story.LIMITATIONS["anchor"])
with st.expander(story.LIMITATIONS["title"], expanded=True):
    st.markdown(story.LIMITATIONS["body"])

# Render the conclusion section
section_card(story.CONCLUSION["title"], story.CONCLUSION["body"])