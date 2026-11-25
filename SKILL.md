---
name: pollinations-poster-studio
description: Make a finished poster image with Pollinations from a short brief. Use when the user asks for a poster, cover art, social card, or event graphic and wants an image generated plus a matching caption.
---

# Pollinations Poster Studio

Turn a one-line brief into a poster image and a ready-to-post caption using Pollinations models.

## Workflow

1. Ask for the brief if it is missing: subject, mood, any text that must appear, and the size or platform.
2. Write a tight image prompt: subject, style, lighting, composition, and the exact words to render. Keep rendered text short; image models mangle long text.
3. Generate the image with `scripts/make_poster.py`, which calls the Pollinations image API with the user's own key from the `POLLINATIONS_API_KEY` environment variable. Never ask the user to paste a key into chat; tell them to set the environment variable or sign in with Pollinations.
4. Show the image, then write a caption in the user's language with two or three fitting hashtags.
5. Offer one variation: a different mood, crop, or color palette. Regenerate only when the user asks.

## Rules

- Use the user's own Pollinations balance. State the model and size before generating when the user cares about cost.
- Default model: `black-forest-labs/flux.1-schnell` for fast drafts. Use a stronger image model only when the user asks for higher quality.
- If generation fails, say what failed and retry once with a simpler prompt.
- Keep people, brands, and copyrighted characters out of prompts unless the user supplied the reference and has the rights to use it.
