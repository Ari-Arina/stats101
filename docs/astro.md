# What is Astro?

"Astro is the web framework for building content-driven websites like blogs, marketing, and e-commerce. Astro is best-known for pioneering a new frontend architecture to reduce JavaScript overhead and complexity compared to other frameworks. If you need a website that loads fast and has great SEO, then Astro is for you." - [Astro](https://docs.astro.build/en/concepts/why-astro/)

A framework I like to use due to its organization and loading speed!

# How to make an Astro Website

Write in your terminal the following:
``npm create astro@latest``

Either configure directory to your project or move files from folder to main project.


## Updating Astro
Important - not updating can mean that program will not work.

In case of Astro updates, run the following command:
``npx @astrojs/upgrade``
 or
 ``npm install -g npm@__.__.__`` 
 (blank spaces are the version available)

## How to run Astro

In the terminal you can type the following command to see your local link for your project:
``npm run dev``

# Astro Structure

Under the folder `src` is the folder where you will work on the most. It has the following folders:

- `assets`: any pictures, svgs, or assets you will use can be put here!
- `components`: this is where you store `.astro` files and create specific sections of your program (footer, header, a specific section in a page, etc.).
- `layouts`:  this is a way to make a general layout for different pages and keep everything organized. Files are `.astro`.
- `pages`: here you will create `.astro` files, these are the different pages that will be in your website.

Additional folders you can create:
- `styles`: any global style overall can be coded here, here you would put `css` files or `react`.
- `scripts`: any scripts you need to make can be put here. 

**Astro Readme Tutorial:**

---

# Astro Starter Kit: Basics

```sh
npm create astro@latest -- --template basics
```

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
│   └── favicon.svg
├── src
│   ├── assets
│   │   └── astro.svg
│   ├── components
│   │   └── Welcome.astro
│   ├── layouts
│   │   └── Layout.astro
│   └── pages
│       └── index.astro
└── package.json
```

To learn more about the folder structure of an Astro project, refer to [our guide on project structure](https://docs.astro.build/en/basics/project-structure/).

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).