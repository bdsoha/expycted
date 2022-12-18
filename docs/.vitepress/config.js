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
        text: 'Introduction',
        items: [
          { text: 'What is Expycted?', link: '/introduction/what-is-expycted' },
          { text: 'Installation', link: '/introduction/installation' },
          { text: 'Getting Started', link: '/introduction/getting-started' },
        ]
      },
      {
        text: 'Expectations',
        items: [
          { text: 'Overview', link: '/expectations/overview'},
          { text: 'Strict Mode', link: '/expectations/strict-mode'},
          { text: 'Higher Order Expectations', link: '/expectations/higher-order-expectations'}
        ]
      },
      {
        text: 'Interface',
        collapsible: true,
        collapsed: true,
        items: [
          { text: 'Expectations', link: '/expectations/interface/expectations'},
          { text: 'Filesystem', link: '/expectations/interface/filesystem'},
          { text: 'Function', link: '/expectations/interface/function'},
        ]
      },
      {
        text: 'Get Involved',
        items: [
          { text: 'Introduction', link: '/contribute/introduction' },
          { text: 'Development Install', link: '/contribute/development-install' },
          { text: 'Contribution Workflow', link: '/contribute/contribution-workflow' },
          { text: 'Pull Request Guidelines', link: '/contribute/pull-request-guidelines' },
        ]
      }
    ]
  }
}