import os
import re
from pathlib import Path

ROOT = Path(".")
MKDOCS = ROOT / "mkdocs.yml"
PROJECTS_DIR = ROOT / "docs" / "projects"

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text[:80].strip("-") or "project"

def split_list(val: str, sep: str = ","):
    if not val:
        return []
    return [x.strip() for x in val.split(sep) if x.strip()]

def split_semicolon_items(val: str):
    if not val:
        return []
    return [x.strip() for x in val.split(";") if x.strip()]

def ensure_files():
    if not MKDOCS.exists():
        raise SystemExit("mkdocs.yml not found")
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)

def generate_md(title, date, repo_url, demo_url, skills, description, components, structure, workflow_image, example_images, slug):
    md_path = PROJECTS_DIR / f"{slug}.md"

    skills_list = split_list(skills, ",")
    components_list = split_semicolon_items(components) if ";" in components else split_list(components, ",")
    structure_list = split_semicolon_items(structure)

    example_list = split_list(example_images, ",") if example_images else []

    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"*Date of creation: {date}*")
    lines.append("")
    lines.append("## Project description")
    lines.append(description.strip())
    lines.append("")
    lines.append("**Key components of the project:**")
    lines.append("")
    for item in components_list:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Skills")
    lines.append("")
    for s in skills_list:
        lines.append(f"- **{s}**")
    lines.append("")
    lines.append("## Project structure")
    lines.append("")
    lines.append("The project consists of several essential files, each responsible for a specific part of the workflow:")
    lines.append("")
    for item in structure_list:
        lines.append(f"- {item}")
    lines.append("")
    if workflow_image:
        lines.append("## Project workflow")
        lines.append("")
        lines.append(f"![Project workflow](../{workflow_image})")
        lines.append("")
    if example_list:
        lines.append("## Example Images from Application in Use")
        lines.append("")
        for img in example_list:
            lines.append(f"![APP](../{img})")
        lines.append("")
    lines.append("## Explore the app:")
    lines.append("")
    lines.append(f'[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?logo=github)]({repo_url})')
    if demo_url:
        lines.append("&nbsp;")
        lines.append(f'[![Open in Streamlit](https://img.shields.io/badge/Open%20in-Streamlit-ff4b4b?logo=streamlit&logoColor=white)]({demo_url})')
    lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return md_path

def update_mkdocs_nav(title: str, slug: str):
    content = MKDOCS.read_text(encoding="utf-8").splitlines()

    project_line = f'      - "{title}": projects/{slug}.md'
    if any(project_line == line for line in content):
        return

    idx_projects = None
    last_proj_idx = None
    for idx, line in enumerate(content):
        if line.strip() == "- Projects:":
            idx_projects = idx
            continue
        if idx_projects is not None:
            if re.match(r'^\s{6}-\s+".*":\s+projects\/.*\.md\s*$', line):
                last_proj_idx = idx
            if idx > idx_projects and re.match(r'^\s{2}-\s+', line) and not line.strip().startswith("- Projects:"):
                break

    if last_proj_idx is None:
        content.append(project_line)
    else:
        content.insert(last_proj_idx + 1, project_line)

    MKDOCS.write_text("\n".join(content) + "\n", encoding="utf-8")

def main():
    ensure_files()

    title = os.environ["TITLE"]
    date = os.environ["DATE"]
    repo_url = os.environ["REPO_URL"]
    demo_url = os.environ.get("DEMO_URL", "").strip()
    skills = os.environ["SKILLS"]
    description = os.environ["DESCRIPTION"]
    components = os.environ["COMPONENTS"]
    structure = os.environ["STRUCTURE"]
    workflow_image = os.environ.get("WORKFLOW_IMAGE", "").strip()
    example_images = os.environ.get("EXAMPLE_IMAGES", "").strip()
    slug = os.environ.get("SLUG", "").strip() or slugify(title)

    generate_md(
        title=title,
        date=date,
        repo_url=repo_url,
        demo_url=demo_url,
        skills=skills,
        description=description,
        components=components,
        structure=structure,
        workflow_image=workflow_image,
        example_images=example_images,
        slug=slug,
    )
    update_mkdocs_nav(title=title, slug=slug)
    print(f"Generated docs/projects/{slug}.md and updated mkdocs.yml")

if __name__ == "__main__":
    main()
