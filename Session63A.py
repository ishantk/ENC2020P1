from flask import *

# Creating a Python App running on Flask Server
app = Flask("LMS")

# We may have multiple roles for a Learning Management System
# Roles: student, teacher, parent, admin

@app.route("/student")
def student():

    # html = """
    #             <html>
    #                 <body>
    #                     <center>
    #                         <br/>
    #                         <h3>Welcome to LMS</h3>
    #                         <h4>Dear Student, Please Login Below:</h4>
    #                         <form>
    #                             <input type='text' placeholder='Enter Your Email'/>
    #                             <input type='password' placeholder='Enter Your Password'/>
    #                             <input type='submit' value='Login'/>
    #                         </form>
    #                     </center>
    #                 </body>
    #             </html>
    #           """
    # return html

    return render_template("student.html")


@app.route("/teacher")
def teacher():

    html = """
                <html>
                    <body>
                        <center>
                            <br/>
                            <h3>Welcome to LMS</h3>
                            <h4>Dear Teacher, Please Login Below:</h4>
                            <form>
                                <input type='text' placeholder='Enter Your Email'/>
                                <input type='password' placeholder='Enter Your Password'/>
                                <input type='text' placeholder='Enter OTP'/>
                                <input type='submit' value='Login'/>
                            </form>
                        </center>
                    </body>
                </html>
              """
    return html

@app.route("/parent")
def parent():

    html = """
                <html>
                    <body>
                        <center>
                            <br/>
                            <h3>Welcome to LMS</h3>
                            Everything Seems Good. Thank You for Connecting with Us !!
                        </center>
                    </body>
                </html>
              """
    return html

@app.route("/admin")
def admin():

    html = """
                <html>
                    <body>
                        <center>
                            <br/>
                            <h3>Welcome to LMS</h3>
                            <h4>Dear ADMIN, Please Login Below:</h4>
                            <form>
                                <input type='text' placeholder='Enter Your Email'/>
                                <input type='captcha' placeholder='Enter the Code'/>
                                <input type='password' placeholder='Enter Your Password'/>
                                <input type='text' placeholder='Enter OTP'/>
                                <input type='submit' value='Login'/>
                            </form>
                        </center>
                    </body>
                </html>
              """
    return html


@app.route("/")
def home():
    return "<h3>WELCOME TO LMS</h3>"

@app.route("/<type>")
def user(type):
    if type == "student":
        return redirect(url_for("student"))
    elif type == "teacher":
        return redirect(url_for("teacher"))
    elif type == "parent":
        return redirect(url_for("parent"))
    elif type == "admin":
        return redirect(url_for("admin"))
    else:
        return "INVALID REQUEST"

if __name__ == '__main__':
    app.run(debug=True)