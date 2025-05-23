
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
  

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+pg8000://librarysdb_user:I1FCS3WWae7KSZ8rEvyxITw7gCW6Otey@dpg-d0o9v8mmcj7s73e9usvg-a:5432/librarysdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class SupportAdmin(db.Model):
    __tablename__ = 'super_admins'  # اسم الجدول في قاعدة البيانات
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    section = db.Column(db.String(100), nullable=False)



class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=True)
    year = db.Column(db.String(10), nullable=True)
    category_number = db.Column(db.String(50), nullable=True)
    shelf_location = db.Column(db.String(50), nullable=True)
    book_number_on_shelf = db.Column(db.String(50), nullable=True)
    publisher = db.Column(db.String(100), nullable=True)
    is_borrowed = db.Column(db.Boolean, default=False)

class EducationalMedia(db.Model):
    __tablename__ = 'educational_media'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=True)
    year = db.Column(db.String(10), nullable=True)
    category_number = db.Column(db.String(50), nullable=True)
    shelf_location = db.Column(db.String(50), nullable=True)
    book_number_on_shelf = db.Column(db.String(50), nullable=True)
    publisher = db.Column(db.String(100), nullable=True)
    is_borrowed = db.Column(db.Boolean, default=False)

class Artia(db.Model):
    __tablename__ = 'artia'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=True)
    year = db.Column(db.String(10), nullable=True)
    category_number = db.Column(db.String(50), nullable=True)
    shelf_location = db.Column(db.String(50), nullable=True)
    book_number_on_shelf = db.Column(db.String(50), nullable=True)
    publisher = db.Column(db.String(100), nullable=True)
    is_borrowed = db.Column(db.Boolean, default=False)

class HomeEconomics(db.Model):
    __tablename__ = 'home_economics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=True)
    year = db.Column(db.String(10), nullable=True)
    category_number = db.Column(db.String(50), nullable=True)
    shelf_location = db.Column(db.String(50), nullable=True)
    book_number_on_shelf = db.Column(db.String(50), nullable=True)
    publisher = db.Column(db.String(100), nullable=True)
    is_borrowed = db.Column(db.Boolean, default=False)

class MusicalEducationMedia(db.Model):
    __tablename__ = 'musical_education_media'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=True)
    year = db.Column(db.String(10), nullable=True)
    category_number = db.Column(db.String(50), nullable=True)
    shelf_location = db.Column(db.String(50), nullable=True)
    book_number_on_shelf = db.Column(db.String(50), nullable=True)
    publisher = db.Column(db.String(100), nullable=True)
    is_borrowed = db.Column(db.Boolean, default=False)

class PostGraduateLibrary(db.Model):
    __tablename__ = 'post_graduate_library'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=True)
    year = db.Column(db.String(10), nullable=True)
    category_number = db.Column(db.String(50), nullable=True)
    shelf_location = db.Column(db.String(50), nullable=True)
    book_number_on_shelf = db.Column(db.String(50), nullable=True)
    publisher = db.Column(db.String(100), nullable=True)
    is_borrowed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

# ====== الصفحات العامة ======

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tech')
def tech_section():
    query = request.args.get('query', '').strip()
    if query:
        books = Book.query.filter(
            (Book.title.ilike(f"{query}%")) |
            (Book.author.ilike(f"{query}%")) |
            (Book.publisher.ilike(f"{query}%")) |
            (Book.shelf_location.ilike(f"%{query}%")) |
            (Book.category_number == query) |
            (Book.book_number_on_shelf == query) |
            (Book.year == query)
        ).all()
    else:
        books = Book.query.all()
    return render_template('public.html', books=books)

@app.route('/media')
def media_section():
    query = request.args.get('query', '').strip()
    if query:
        media_items = EducationalMedia.query.filter(
            (EducationalMedia.title.ilike(f"{query}%")) |
            (EducationalMedia.author.ilike(f"{query}%")) |
            (EducationalMedia.publisher.ilike(f"{query}%")) |
            (EducationalMedia.shelf_location.ilike(f"%{query}%")) |
            (EducationalMedia.category_number == query) |
            (EducationalMedia.book_number_on_shelf == query) |
            (EducationalMedia.year == query)
        ).all()
    else:
        media_items = EducationalMedia.query.all()
    return render_template('media_section.html', media_items=media_items)

@app.route('/art_education')
def art_education_section():
    query = request.args.get('query', '').strip()
    if query:
        art_items = Artia.query.filter(
            (Artia.title.ilike(f"{query}%")) |
            (Artia.author.ilike(f"{query}%")) |
            (Artia.publisher.ilike(f"{query}%")) |
            (Artia.shelf_location.ilike(f"%{query}%")) |
            (Artia.category_number == query) |
            (Artia.book_number_on_shelf == query) |
            (Artia.year == query)
        ).all()
    else:
        art_items = Artia.query.all()
    return render_template('art_education_section.html', art_items=art_items)

@app.route('/homeeconomics')
def home_economics_section():
    query = request.args.get('query', '').strip()
    if query:
        home_items = HomeEconomics.query.filter(
            (HomeEconomics.title.ilike(f"{query}%")) |
            (HomeEconomics.author.ilike(f"{query}%")) |
            (HomeEconomics.publisher.ilike(f"{query}%")) |
            (HomeEconomics.shelf_location.ilike(f"%{query}%")) |
            (HomeEconomics.category_number == query) |
            (HomeEconomics.book_number_on_shelf == query) |
            (HomeEconomics.year == query)
        ).all()
    else:
        home_items = HomeEconomics.query.all()
    return render_template('home_section.html', home_items=home_items)

@app.route('/musical')
def musical_section():
    query = request.args.get('query', '').strip()
    if query:
        media_items = MusicalEducationMedia.query.filter(
            (MusicalEducationMedia.title.ilike(f"{query}%")) |
            (MusicalEducationMedia.author.ilike(f"{query}%")) |
            (MusicalEducationMedia.publisher.ilike(f"{query}%")) |
            (MusicalEducationMedia.shelf_location.ilike(f"%{query}%")) |
            (MusicalEducationMedia.category_number == query) |
            (MusicalEducationMedia.book_number_on_shelf == query) |
            (MusicalEducationMedia.year == query)
        ).all()
    else:
        media_items = MusicalEducationMedia.query.all()
    return render_template('musical.html', media_items=media_items)

@app.route('/postgraduate')
def post_graduate_section():
    query = request.args.get('query', '').strip()
    if query:
        post_items = PostGraduateLibrary.query.filter(
            (PostGraduateLibrary.title.ilike(f"{query}%")) |
            (PostGraduateLibrary.author.ilike(f"{query}%")) |
            (PostGraduateLibrary.publisher.ilike(f"{query}%")) |
            (PostGraduateLibrary.shelf_location.ilike(f"%{query}%")) |
            (PostGraduateLibrary.category_number == query) |
            (PostGraduateLibrary.book_number_on_shelf == query) |
            (PostGraduateLibrary.year == query)
        ).all()
    else:
        post_items = PostGraduateLibrary.query.all()
    return render_template('postgraduate_section.html', post_items=post_items)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # البحث في جدول الأدمن الرئيسي (SupportAdmin)
        super_admin = SupportAdmin.query.filter_by(username=username, password=password).first()
        if super_admin:
            session['super_admin_id'] = super_admin.id
            session['role'] = 'super'
            return render_template('dashboard.html')  # يفتح صفحة السبورت أدمن

        # البحث في جدول أدمنات الأقسام (Admin)
        admin = Admin.query.filter_by(username=username, password=password).first()
        if admin:
            session['admin_id'] = admin.id
            session['section'] = admin.section
            session['role'] = 'section'
            return redirect('/admin_panel')

        flash('اسم المستخدم أو كلمة السر غير صحيحة')
        return redirect('/login')

    return render_template('login.html')




@app.route('/admin_panel')
def admin_panel():
    if 'admin_id' not in session:
        return redirect('/login')

    section = session.get('section')
    show_borrowed = request.args.get('show_borrowed') == 'True'  # قراءة المعلمة من الرابط

    # اختيار الجدول بناءً على القسم
    if section == 'tech':
        model = Book
    elif section == 'media':
        model = EducationalMedia
    elif section == 'art_education':
        model = Artia
    elif section == 'homeeconomics':
        model = HomeEconomics
    elif section == 'musical':
        model = MusicalEducationMedia
    elif section == 'postgraduate':
        model = PostGraduateLibrary
    else:
        books = []
        model = None

    # جلب البيانات حسب الحالة
    if model:
        if show_borrowed:
            books = model.query.filter_by(is_borrowed=True).all()
        else:
            books = model.query.all()
    else:
        books = []

    return render_template('admin_panel.html', books=books, section=section, show_borrowed=show_borrowed)


@app.route('/edit/<section>/<int:id>', methods=['GET', 'POST'])
def edit_book(section, id):
    table = get_model_by_section(section)
    book = table.query.get_or_404(id)

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.year = request.form['year']
        book.category_number = request.form['category_number']
        book.shelf_location = request.form['shelf_location']
        book.book_number_on_shelf = request.form['book_number_on_shelf']
        book.publisher = request.form['publisher']
        db.session.commit()
        return redirect('/admin_panel')

    return render_template('edit_book.html', book=book, section=section)


@app.route('/add/<section>', methods=['GET', 'POST'])
def add_book(section):
    table = get_model_by_section(section)

    if request.method == 'POST':
        new_book = table(
            title=request.form['title'],
            author=request.form['author'],
            year=request.form['year'],
            category_number=request.form['category_number'],
            shelf_location=request.form['shelf_location'],
            book_number_on_shelf=request.form['book_number_on_shelf'],
            publisher=request.form['publisher']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect('/admin_panel')

    return render_template('add_book.html', section=section)



@app.route('/delete/<section>/<int:id>')
def delete_book(section, id):
    table = get_model_by_section(section)
    book = table.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/admin_panel')



def get_model_by_section(section):
    if section == 'tech':
        return Book
    elif section == 'media':
        return EducationalMedia
    elif section == 'art_education':
        return Artia
    elif section == 'homeeconomics':
        return HomeEconomics
    elif section == 'musical':
        return MusicalEducationMedia
    elif section == 'postgraduate':
        return PostGraduateLibrary
    else:
        return None

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/borrow/<string:table>/<int:item_id>', methods=['POST'])
def mark_as_borrowed(table, item_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))

    # دعم الجداول المختلفة
    models = {
        'Book': Book,
        'EducationalMedia': EducationalMedia,
        'Artia': Artia,
        'HomeEconomics': HomeEconomics,
        'MusicalEducationMedia': MusicalEducationMedia,
        'PostGraduateLibrary': PostGraduateLibrary
    }

    if table not in models:
        flash("الجدول غير مدعوم")
        return redirect(url_for('admin_panel'))

    model = models[table]
    item = model.query.get_or_404(item_id)

    if hasattr(item, 'is_borrowed'):
        item.is_borrowed = True
        db.session.commit()


    return redirect(url_for('admin_panel'))


@app.route('/return/<string:table>/<int:item_id>', methods=['POST'])
def mark_as_returned(table, item_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))

    # دعم الجداول المختلفة
    models = {
        'Book': Book,
        'EducationalMedia': EducationalMedia,
        'Artia': Artia,
        'HomeEconomics': HomeEconomics,
        'MusicalEducationMedia': MusicalEducationMedia,
        'PostGraduateLibrary': PostGraduateLibrary
    }

    if table not in models:
        flash("الجدول غير مدعوم")
        return redirect(url_for('admin_panel'))

    model = models[table]
    item = model.query.get_or_404(item_id)

    if hasattr(item, 'is_borrowed'):
        item.is_borrowed = False
        db.session.commit()


    return redirect(url_for('admin_panel'))

@app.route('/super_admin/dashboard')
def super_admin_dashboard():
    admins = Admin.query.all()   # ← هنا تم تغيير الاسم إلى "admins"
    return render_template('dashboard.html', admins=admins)

@app.route('/super_admin/edit_admin/<int:admin_id>', methods=['GET', 'POST'])
def edit_admin(admin_id):
    if request.method == 'POST':
        admin = Admin.query.get(admin_id)
        admin.username = request.form['username']
        admin.password = request.form['password']
        admin.section = request.form['section']
        db.session.commit()
        return redirect('/super_admin/dashboard')
    else:
        admin = Admin.query.get(admin_id)
        return render_template('edit_admin.html', admin=admin)

@app.route('/super_admin/add_admin', methods=['GET', 'POST'])
def add_admin():
    if request.method == 'POST':
        new_admin = Admin(
            username=request.form['username'],
            password=request.form['password'],
            section=request.form['section']
        )
        db.session.add(new_admin)
        db.session.commit()
        return redirect('/super_admin/dashboard')
    return render_template('add_admin.html')

@app.route('/super_admin/delete_admin/<int:admin_id>')
def delete_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    db.session.delete(admin)
    db.session.commit()
    return redirect('/super_admin/dashboard')

# تنفيذ التطبيق
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
