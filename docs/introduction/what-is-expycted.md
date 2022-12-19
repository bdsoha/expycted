# What is Expycted?

> A quick introduction in to what Expycted is and why it should be used.

Expectations is a simple and human-readable expectation *(assertion)* library. It allows you to write your tests like you would a sentence.
Expycted's API gained much inspiration from [Jest](https://jestjs.io/docs/expect) and [Pest](https://pestphp.com/docs/expectations).

<hr /> 

## Frequently asked questions

#### Is Expycted Framework specific?
**No**, Expycted is framework agnostic and can be used in any Python project, be it a new or existing. Our internal tests are run with `pytest` due to preference only, but you can choose whatever suites your needs.

#### Can I use my existing test case and layouts?
**Yes**, Expycted is opt-in. It allows you to use both *native* Python `assert` statements alongside `expect()` statements, in the same test. Choose to use Expycted project-wide, in a single-test suite, or even in a single test function.

#### Is Expycted open source?
**Yes**, Expycted is an open-sourced software licensed under the MIT license. Constibutions are always welcome!
