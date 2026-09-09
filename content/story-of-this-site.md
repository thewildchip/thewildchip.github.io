+++
title = "story of this site"
description = "How and why I built this."
page_class = "story-page"
+++

**F\*ck React – A Minimalist's Homepage**  
[Source code](https://github.com/thewildchip/thewildchip.github.io)

_(clickbait title haha)_

Anyone who is interested in AI knows Andrej Karpathy. While reading through [his homepage](https://karpathy.ai/) (last visited: 09/09/26), I stumbled upon this paragraph:

> 0 frameworks were used to make this simple responsive website because I am becoming seriously allergic to 500-pound websites. This one is pure HTML and CSS in two static files and that's it.

I found that interesting because I thought personal pages had to be flashy and have trending effects. For me, that was the barrier to publishing my own website, as I absolutely **hate** JS and these frontend libraries (nothing against people who love such things).

This led me to find the best static site generator for my needs: [Hugo](https://github.com/gohugoio/hugo), paired with [this template](https://github.com/ntk148v/shibui) – shoutout to ntk148v for this amazing 🪄 minimal theme.

One of Hugo's biggest benefits is that you can edit your content using Markdown files in `/content/`. Theme customizations are also easy, as you only need to edit `/assets/css/custom.css` to override the default styles in `/assets/css/main.css`. Layouts can be customized in `/layouts/`, while further configuration can be changed in `hugo.toml`.

After that, I roughly designed (picture below) how I wanted the website to look and customized the theme and layout with the assistance of [Hermes](https://hermes-agent.nousresearch.com/), and of course filled in the content myself. Also, thanks to [Nous Research](https://nousresearch.com/) for the color inspiration.


