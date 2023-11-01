<h1>Django Project with VirtualEnv, Decouple, Docker and API REST</h1>

<p>This is a Django project template that incorporates VirtualEnv for environment isolation, Decouple for managing configurations, and Docker for containerization.</p>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
    <li>Python 3.10</li>
    <li>Docker</li>
</ul>

<h3>Installing</h3>
<ol>
<li>Clone the repository to your local machine:</li>
<pre><code>git clone https://github.com/GDS2005/pharmatube.git</code></pre>

<li>Navigate to the project directory:</li>
<pre><code>cd pharmatube</code></pre>

<li>Create a virtual environment:</li>
<pre><code>python3 -m venv venv</code></pre>

<li>Activate the virtual environment:</li>
<pre><code>source venv/bin/activate   <!-- On Windows, use `venv\Scripts\activate` --></code></pre>

<li>Install project dependencies:</li>
<pre><code>pip install -r requirements.txt</code></pre>

<li>Create a <code>.env</code> file using the provided <code>.env.example</code> template:</li>
<pre>
    <code>
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=my_database
    DB_USER=my_user
    DB_PASSWORD=my_password
    </code>
</pre>

<li>Edit the <code>.env</code> file with your specific configuration settings.</li>

<li>Needed if we make some changes in the code.</li>
<pre><code>python manage.py makemigrations</code></pre>

<li>Migrate to create the table with the models configuration.</li>
<pre><code>python manage.py migrate</code></pre>

</ol>

<h2>Running with Docker</h2>
<ol>
<li>Build the Docker image:</li>
<pre><code>docker build -t pharmatube .</code></pre>

<li>Start the Docker container:</li>
<pre><code>docker run -p 8000:8000 pharmatube</code></pre>
</ol>

<p>The application will be accessible at <a href="http://localhost:8000">http://localhost:8000</a>.</p>

<h2>Development</h2>
<p>While working on the project, ensure that the virtual environment is activated. You can run the Django development server using the following command:</p>
<pre><code>python manage.py runserver</code></pre>

<h2>Running Tests</h2>
<p>You can run the project's tests using:</p>
<pre><code>python manage.py test</code></pre>

<h2>Deployment</h2>
<p>For deploying the project, you can use your preferred hosting platform and follow their deployment instructions. Ensure to set the environment variables as specified in the <code>.env</code> file.</p>

<h2>Contributing</h2>
<p>Please read <a href="CONTRIBUTING.md">CONTRIBUTING.md</a> for details on our code of conduct, and the process for submitting pull requests to us.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Acknowledgments</h2>
<ul>
    <li><a href="https://docs.djangoproject.com/">Django Documentation</a></li>
    <li><a href="https://github.com/henriquebastos/python-decouple">python-decouple</a></li>
</ul>