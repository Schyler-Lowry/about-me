<<<<<<< HEAD
# Assignment 1 - Static Web Site In Django

## Author



## Description

Create a Django Web Application with a few static pages about yourself using Bootstrap for styling. There will be three pages in total that all extend a base template. Once created, you will add testing to make sure all pages work and then host it on heroku.

The first page will be an informal resume like page about yourself. This should be the main default page when first visiting the site. I'm not looking for a resume, but more like an introduction to yourself. Frame it in a professional manner though. Think of it as a supplemental thing that you could use when applying for a job. If you want some inspiration, you can take a look at mine at: http://barnesbrothers.net though mine includes essentially all three of these separate pages in a single one.

The next page will be a projects page listing the various programming projects you have worked on. More than likely this will be class assignments you have done thus far. The point though is to showcase what you are capable of. Since we haven't seen how to do static asset loading like images yet, you obviously won't be able to include any images (unless you want to figure that out or they are already hosted somewhere on the internet for easy loading). We will cover that in a later chapter, but for now, using just text is okay. If you were smart though, you would design the page in such a way so that when we learn how to add images, you could make a quick update to this assignment to include images and have a professional site about yourself.

The last page will be a contact page on how to get in contact with you. This could include links to your LinkedIn, Github, and other platforms that are relevant. In addition, it ought to have the standard contact information so that potential employers can reach you. In the sample I linked above, I included a form. You do not need to do this.

I am not expecting that your site will look like mine, but I am expecting that you will use Bootstrap. My site uses custom CSS, so, I find it unlikely that you could make it look like mine even if you wanted it to since we don't know how to load our own CSS and JS files yet. Below there are links to Bootstrap documentation that should come in handy.

Tests for the site should be similar to the ones we wrote in class. I am expecting 4 per page for a total of 12. Just like what we did in the in-class.

Publish the site on Heroku and submit the URL for the site to Canvas as the submission for this assignment.

Ensure that you have a `requirements.txt` file with your required packages. I will not grade the assignment if I can't restore the packages easily!

The program should allow the following functionality:

1. Created Django Project and App for static pages.
2. Base template that other templates will extend from.
3. Three Urls/Views/Templates for site.
   1. Home route with an index page that is about yourself. Informal Resume.
   2. A page with projects you have worked on.
   3. A page with contact information.
4. Basic Bootstrap styling.
5. 4 Tests for each page. (12 in total) To ensure loading of pages works. For each page test:
   1. URL exists at correct location.
   2. URL available by name.
   3. Template name is correct.
   4. Template content is correct.
6. Published to Heroku and URL submitted to Canvas as Assignment Submission.
7. Ensure `requirements.txt` is included in your project.

Documentation should include the following for this, and all future assignments:
* Comments at the top of each file that you add source code to with the following:
  * Your Name
  * Class
  * Date
* A comment after the definition of each method describing what it does. Use the """ (triple quote) doc string method for the comment.
* Comments in the rest of the code where it isn't obvious what is going on. (I prefer above the line comments vs at the end of the line because who likes to horizontally scroll, but either will work)

Solution Requirements:

* Created Django Project and App for static pages.
* Base template that other templates will extend from.
* Three Urls/Views/Templates for site.
* Basic Bootstrap styling.
* Tests to ensure loading of pages works.
* Published to Heroku and URL submitted to Canvas as Assignment Submission.

### Notes
I would like you to use Bootstrap, the following links may be useful creating your pages.
It provides a few Examples using Bootstrap that could be tailored to this application.
You may not need every single part of the example, but you could view the source and use the parts that make sense for your site. Even just the act of loading Bootstrap will give you an improvement over the default browser styling.
Since we haven't covered how to load our own CSS yet, this will be your best option to make it look reasonable.

https://getbootstrap.com/docs/5.2/examples/sticky-footer-navbar/

and / or

https://getbootstrap.com/docs/5.2/examples/jumbotron/

If you do not like that template, you can see all available examples here:

https://getbootstrap.com/docs/5.2/examples/

In addition, you can find the documentation for Bootstrap here:

https://getbootstrap.com/docs/5.2/getting-started/introduction/

You will need load Bootstrap via a CDN link since we don't know how to manually add static files yet.
This means having lines similar to the following in your base template.

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
```

## Grading
| Feature                                  | Points |
|------------------------------------------|--------|
| Create Django Project and App            | 10     |
| Base Template                            | 10     |
| Home Url/View/Template                   | 15     |
| Projects URL/View/Template               | 15     |
| Contact URL/View/Template                | 15     |
| Bootstrap Styling                        | 10     |
| Automated Tests                          | 10     |
| Heroku Deployment                        |  5     |
| Documentation                            |  5     |
| Readme                                   |  5     |
| **Total**                                | **100**|

## Outside Resources Used



## Known Problems, Issues, And/Or Errors in the Program


=======
# about-me
>>>>>>> 004144b7caac4709ef90a36a93b3d9777ef545c1
