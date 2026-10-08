# Assets

Recommended structure for the site's public files:

- `css/`: compiled or site-specific styles.
- `js/`: the site's own scripts.
- `vendor/`: third-party libraries. Do not mix your own code here.
- `documents/cv/`: CVs and downloadable professional documents.
- `documents/certificates/`: certificate and diploma PDFs.
- `images/brand/`: logo, cover, visual identity and global brand assets.
- `images/profile/`: photos, avatars and personal images.
- `images/blog/`: featured images for posts.
- `images/blog/tutorials/`: screenshots and inline tutorial images.
- `images/portfolio/`: project and case-study images.
- `images/certificates/`: certificate and diploma images.
- `images/logos/tech/`: technology and tool logos.
- `images/logos/brands/`: brand or client logos.
- `images/logos/clients/`: client logos used by templates or legacy sections.

Good practices:

- Use lowercase, hyphen-separated names for new files.
- Avoid spaces and accents in new file names where possible.
- Keep PDFs in `documents/`, not in `images/`.
- Keep third-party assets inside `vendor/`.
- Use the `relative_url` Liquid filter so GitHub Pages respects `baseurl`.
