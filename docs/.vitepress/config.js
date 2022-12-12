const git_url = 'https://github.com/bdsoha/expycted'

export default {
  title: 'Expycted',
  description: 'Because tests should be easy to read.',

  themeConfig: {

    socialLinks: [
        { icon: 'github', link: git_url },
    ],

    editLink: {
        pattern: `{git_url}/edit/master/docs/:path`,
        text: 'Edit this page on GitHub'
    },

    sidebar: [
      {
        text: 'Guides',
        items: [
          { text: 'Installation', link: '/guides/installation' },
          { text: 'Getting Started', link: '/guides/getting-started' },
        ]
      },
      {
        text: 'Contribute',
        items: [
          { text: 'Contribute', link: '/contribute/contribute' },
        ]
      }
    ]
  }
}