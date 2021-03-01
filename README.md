## Olo Offline Automation Challenge:

As a Software Engineer in Test at Olo, your primary responsibility will be developing automated tests at the API and UI level. We expect our engineers to be able to architect well designed test plans, develop well organized, DRY, and reliable automated tests, and to help identify design flaws with applications under development.

Create a public github repo to complete the following assignment. When complete, please reply to this email with the github url.

In one of the following languages (C#, javascript, java, ruby, python, f#) develop a suite of automated API tests against the following API endpoints. You are free to architect your solution in any way you want, but should be prepared to justify and explain why you built it the way you did. It is more important to have well designed code than to complete every item. You should use this exercise as an opportunity to demonstrate to Olo your recommended approach for automation of an API, and your technical acumen. If you are unable to complete your test suite to your satisfaction, be prepared to explain what additional functionality you would want to include, and how much time you feel you would require to finish it.

Bonus points if you identify any defects or functional gaps of the application under test, or can identify architectural issues with how the API is designed. We will discuss these issues in person during the next interview, and will ask you to modify your code base to support some additional requirements.

You do not need to complete all items. It’s more important to have a well designed solution and to demonstrate technical competency than to cover every test case or meet all acceptance criteria.

The API is defined here https://jsonplaceholder.typicode.com/guide

- GET https://jsonplaceholder.typicode.com/posts
- POST https://jsonplaceholder.typicode.com/posts
- PUT https://jsonplaceholder.typicode.com/posts/{postId}
- DELETE https://jsonplaceholder.typicode.com/posts/{postId}
- POST https://jsonplaceholder.typicode.com/posts/{postId}/comments
- GET https://jsonplaceholder.typicode.com/comments?postId={postId}

### Acceptance Criteria: (in order of precedence)

- The code base is well organized, DRY, easily readable and appropriately commented
- The project’s git commit history is well commented and easy to understand.
- The tests are reliable, and can be executed numerous times in a row without failures
- Happy path tests were built for all major endpoints
- Negative path tests were built testing for standard failures
- Tests have detailed logs or reports helping to troubleshoot failures
- Tests can be executed in parallel
- Tests are data driven for maximum coverage

# Solution

## Author: Md Mahbubur Rahman