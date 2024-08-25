# CS340
<b>How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?</b><br/> <br/>
When working on readable and adaptable code it is important to understand the customers needs. When working ont his project we wanted to create a CRUD for mongoDB that we could easily use with whatever dashboard we wanted to build.
What makes a good CRUD model would be that we do not really specifcally define anything as a constant. all variables that we use can be changed to work for any DB that use mongo. It is also good practice to comment code especially if any of that code is performing calculations.
This CRUD module would be easily resused by swapping the username, password, host, port, DB, and COL variables to a different DB that I may work on in the furture. <br/>

<br/><b>How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?</b>

The way that I approach a problem is to see how I can break it down. We also want to consider the customer's requirements, and any constraints that they may have. When looking into this dashboard project it was important to analyze what the customer wanted. We also wanted
to make sure that the functianlity was there but also that the UI would not be to much to understand. It is important that we know how to balance items, while also delivering the functinality that we have been asked to create. The difference in planning for this project versus
other projects from previous classes would be laying out how I wanted the dashboard to look. I also had to plan on pulling data from a DB instead of having it sotred locally. 

<br/><b>What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better? </b> <br/>
<br/>A computer scientist is there to design, and develop software. They use their knowledge to solve problems that can be translated or software and hardware. For Grazioso Salvare they wanted a database that could help them locate
certain breeds of animals that they could train for rescues. So the first question is how can we get this infomration and translate it to something that Grazioso can see and filter through. That answer would have been a database using a dashboard. The table on the dashboard 
gives us filtering options by using the DB queries that we created. This allows them to find matches for what they are looking for faster.
