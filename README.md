# A Minimalist's Homepage

A fast, minimal Hugo portfolio site for Daniel Panoor's projects, writing, contact information, and public work.

[View the live site](https://thewildchip.github.io/) · [Source code](https://github.com/thewildchip/thewildchip.github.io)

## Overview

This repository powers Daniel Panoor's personal homepage. The site is designed to be simple, readable, and easy to maintain: content lives in Markdown, Hugo builds the static pages, and GitHub Pages publishes the final site automatically from the `main` branch.

## Try it

Open the deployed site here:

https://thewildchip.github.io/

## Features

- Clean personal landing page with links to Daniel's work and interests.
- Dedicated pages for CV, contact information, writings, mathematics, AI, physics, and curated learning resources.
- Hugo-powered static build for fast page loads and simple deployment.
- Minimal Shibui-based design with local layout and favicon customizations.
- Automated GitHub Pages deployment through GitHub Actions.
- Checked-in favicon generation workflow for keeping browser and mobile icons consistent.

## Quick start

The production deployment currently uses Hugo `0.164.0` in `.github/workflows/pages.yml`.

To view the site locally:

```bash
git clone --recurse-submodules https://github.com/thewildchip/thewildchip.github.io.git
cd thewildchip.github.io
hugo server
```

Then open the local URL printed by Hugo, usually:

```text
http://localhost:1313/
```

## Requirements

- Hugo `0.164.0` or newer, with the extended build.
- Git, including submodule support.
- Python 3, only if regenerating favicon assets.


## Project structure

```text
content/                 Markdown pages for the live site
layouts/                 Local Hugo layout overrides
static/                  Static assets, favicons, and images
themes/shibui/           Shibui Hugo theme submodule
tools/generate-favicons.py
                         Helper script for generating favicon assets
.github/workflows/pages.yml
                         GitHub Pages build and deployment workflow
hugo.toml                Main Hugo configuration
```

## How it works

The site uses Hugo because a personal portfolio should be fast, durable, and easy to edit without a heavy application stack. Most changes are content changes: editing Markdown files in `content/` is enough to update the public pages.

The visual foundation comes from the Shibui Hugo theme, installed as a Git submodule. Local files in `layouts/`, `static/`, and the root Hugo configuration customize the site without rewriting the theme itself. This keeps the project maintainable: the theme can still be updated separately, while Daniel's content and small design decisions stay in this repository.

Deployment is intentionally simple. Every push to `main` triggers the GitHub Actions workflow, builds the static site with Hugo, and publishes the generated output to GitHub Pages.

## License

The source code in this repository is licensed under the [MIT License](LICENSE).

Personal content, including writing, biographical text, CV material, and personal images, remains © Daniel Panoor unless otherwise stated. Please do not reuse that material without permission.


## Credits

- Built with [Hugo](https://github.com/gohugoio/hugo).
- Uses the [Shibui](https://github.com/ntk148v/shibui) Hugo theme.
- Hosted with [GitHub Pages](https://pages.github.com/).
