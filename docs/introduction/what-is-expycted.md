# What is Expycted?

> A quick introduction into what Expycted is and why it should be used.

Expycted is a modern, fast, simple to use *expectation pattern* for testing Python 3.7+ code bases.
Simply put, it is just an abstraction over the built-in `assert` keyword, with the following features:

- Use human-readable expectation, allowing you to write your tests like you would a sentence.
- Testing framework independent.
- Plugs into any project as-is.

Expycted's API gained much inspiration from [Jest](https://jestjs.io/docs/expect) and [Pest](https://pestphp.com/docs/expectations).

![Code Comparison](/code-comparison.png)

---

## Frequently asked questions

### Is Expycted Framework specific?

**No**, Expycted is framework agnostic and can be used in any Python project, be it a new or existing. Our internal tests are run with `pytest` due to preference only, but you can choose whatever suites your needs.

### Can I use my existing test case and layouts?

**Yes**, Expycted is opt-in. It allows you to use both *native* Python `assert` statements alongside `expect()` statements, in the same test. Choose to use Expycted project-wide, in a single-test suite, or even in a single test function.

### Is Expycted open source?

**Yes**, Expycted is an open-sourced software licensed under the MIT license. Constibutions are always welcome!
