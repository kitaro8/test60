from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post, Focal, Report
from django.contrib.auth.models import User
from .forms import FileForm, ImageForm, NameForm, FocalForm, ContactForm, ReportForm
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse



def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("testdb-home")
      
	form = ContactForm()
	return render(request, "testdb/contact.html", {'form':form})


def upload(request):
	form = FileForm(request.POST, request.FILES)
	form = ImageForm(request.POST, request.FILES)
	form = NameForm(request.POST)
	if request.method =='POST':
		if form.is_valid():
			Region = request.POST['Region']
			upload_image = request.FILES['image']
			upload_file = request.FILES['file']
			lines = upload_file.read()

			station = []
			comp = []
			DIS = []
			AZM = []
			ARR_TIME = []
			RES = []
			PHASE = []
			
			for item in lines.split(b"\n"):

				if b'RMS' in item:
					RMS = item[34:40].strip()
					RMS = RMS.decode()

				elif b'Latitude' in item:
					Latitude = item[32:40].strip()
					Latitude = Latitude.decode()
					lu1 = item[63:73].strip()
					lu1 = lu1.decode()
			        

				elif b'Longitude' in item:
					Longitude = item[32:40].strip()
					Longitude = Longitude.decode()
					lu2 = item[63:73].strip()
					lu2 = lu2.decode()

			        
				elif b'Depth' in item:
					Depth = item[34:40].strip()
					Depth = Depth.decode()

				elif b'Gap' in item:
					Gap = item[36:40].strip()
					Gap = Gap.decode()

				elif b'Event (OCAL)' in item:
					item1 = item[21:31].replace(b" ", b"-")
					item2 = item[32:40].replace(b" ", b":")
					item3 = item[40:44].replace(b" ", b".")
					event = item1 + b" " + item2 + item3
					event = event.decode()
			        
				elif b'Magnitude' in item:
					Magnitude = item[10:12]
					Magnitude = Magnitude.decode()
					


				elif b'KAR2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('KAR2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'SLY1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('SLY1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'AMR2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('AMR2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'AMR1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('AMR1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'BSR1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('BSR1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'BSR2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('BSR2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'NSR1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('NSR1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'NSR2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('NSR2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'NSR3' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('NSR3')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)


				elif b'NSR4' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('NSR4')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'KIR1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('KIR1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'ANB1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('ANB1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'DHK1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('DHK1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'SAM1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('SAM1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'DYL1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('DYL1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'BAG1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('BAG1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'KUT1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('KUT1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'TIK1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('TIK1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)				

			current_user = request.user
			upload=Post(RMS=RMS, 
				lu1=lu1, lu2=lu2, 
				Latitude=Latitude, 
				Longitude=Longitude, 
				Depth=Depth, 
				event=event, 
				Gap=Gap, 
				Magnitude=Magnitude, 
				Region=Region, 
				image=upload_image, 
				station=station, 
				comp=comp, 
				DIS=DIS, 
				AZM=AZM, 
				ARR_TIME=ARR_TIME, 
				RES=RES, 
				PHASE=PHASE, 
				file=upload_file, 
				author=current_user, date_posted=event)
			upload.save()
			

	return render(request, 'testdb/post_form.html')



def upload_focal(request):
	form = FocalForm(request.POST, request.FILES)
	if request.method =='POST':
		if form.is_valid():
			title = request.POST['title']
			date = request.POST['date']
			file = request.FILES['file']

			current_user = request.user
			upload=Focal(title=title, file=file, author=current_user, date_posted=date, date=date)
			upload.save()
	return render(request, 'testdb/focal_form.html')


def upload_report(request):
	form = ReportForm(request.POST, request.FILES)
	if request.method =='POST':
		if form.is_valid():
			title = request.POST['title']
			date = request.POST['date']
			file = request.FILES['file']

			current_user = request.user
			upload=Report(title=title, file=file, author=current_user, date_posted=date, date=date)
			upload.save()
	return render(request, 'testdb/report_form.html')


def search_focal(request):

	template = 'testdb/focal.html'

	datef = request.GET.get('datef')
	datet = request.GET.get('datet')

	if datef and datet:
		results = Focal.objects.filter(
			Q(date_posted__gte=datef) & Q(date_posted__lte=datet) 
			)
	else:
		results = Focal.objects.all()

	print(results)

	context = {
		'focal': results
	}
	return render(request, template, context)



def search_posts(request):

	template = 'testdb/search.html'

	datef = request.GET.get('datef')
	datet = request.GET.get('datet')

	Magnitudef = request.GET.get('Magnitudef')
	Magnitudet = request.GET.get('Magnitudet')

	Latitudef = request.GET.get('Latitudef')
	Latitudet = request.GET.get('Latitudet')

	Longitudef = request.GET.get('Longitudef')
	Longitudet = request.GET.get('Longitudet')

	Depthf = request.GET.get('Depthf')
	Deptht = request.GET.get('Deptht')

	search = {
		'datef':datef,
		'datet':datet,
		'Latitudef':Latitudef,
		'Latitudet':Latitudet,
		'Longitudef':Longitudef,
		'Longitudet':Longitudet,
	}

	search1 = {
		'Magnitudef':Magnitudef,
		'Magnitudet':Magnitudef,
		'Depthf':Depthf,
		'Deptht':Deptht
	}


	if search:
		results = Post.objects.filter(
			Q(date_posted__gte=datef), Q (date_posted__lte=datet)
			& Q(Latitude__gte=Latitudef), Q(Latitude__lte=Latitudet)
			& Q(Longitude__gte=Longitudef), Q(Longitude__lte=Longitudet)
			)

	elif search1:
		results = Post.objects.filter(
			Q(date_posted__gte=datef), Q (date_posted__lte=datet)
			& Q(Latitude__gte=Latitudef), Q(Latitude__lte=Latitudet)
			& Q(Longitude__gte=Longitudef), Q(Longitude__lte=Longitudet)
			& Q(Magnitude__gte=Magnitudef), Q(Magnitude__lte=Magnitudet)
			& Q(Depth__gte=Depthf), Q(Depth__lte=Deptht)
			)




	elif Magnitudef and Magnitudet:
		results = Post.objects.filter(
			Q(date_posted__gte=datef), Q (date_posted__lte=datet)
			& Q(Latitude__gte=Latitudef), Q(Latitude__lte=Latitudet)
			& Q(Longitude__gte=Longitudef), Q(Longitude__lte=Longitudet)
			& Q(Magnitude__gte=Magnitudef), Q(Magnitude__lte=Magnitudet)
			)

	elif Depthf and Deptht:
		results = Post.objects.filter(
			Q(date_posted__gte=datef), Q (date_posted__lte=datet)
			& Q(Latitude__gte=Latitudef), Q(Latitude__lte=Latitudet)
			& Q(Longitude__gte=Longitudef), Q(Longitude__lte=Longitudet)
			& Q(Depth__gte=Depthf), Q(Depth__lte=Deptht)
			)


	else:
		results = Post.objects.all()

	context = {
        'posts': results
    }

	return render(request, template, context)



def home(request):
	context = {
        'posts': Post.objects.all()
    }
	return render(request, 'testdb/home.html', context)


def search(request):
	context = {
        'posts': Post.objects.all()
    }
	return render(request, 'testdb/search.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'testdb/home.html'
	context_object_name = 'posts'
	paginate_by = 10


class PostListView3(ListView):
	model = Post
	template_name = 'testdb/search.html'
	context_object_name = 'posts'
	paginate_by = 10

class UserPostListView(ListView):
	model = Post
	template_name = 'testdb/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
	model = Post
	template_name = 'testdb/post_detail.html'


class PostDetailView2(DetailView):
	model = Post
	template_name = 'testdb/post_phase.html'



def focal(request):
	context = {
        'focal': Focal.objects.all()
    }
	return render(request, 'testdb/focal.html', context, {'title': 'Focal Mechanism'})



class PostListView2(ListView):
	model = Focal
	template_name = 'testdb/focal.html'
	context_object_name = 'focal'
	paginate_by = 10

class PostListView4(ListView):
	model = Report
	template_name = 'testdb/report.html'
	context_object_name = 'report'
	paginate_by = 5

# class PostCreateView(LoginRequiredMixin, CreateView):
# 	model = Post
# 	fields = ['image', 'Region']

# CreateView
	

# 	def form_valid(self, form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['RMS',
	'lu1',
	'lu2',
	'Latitude',
	'Longitude',
	'Depth',
	'event',
	'Gap',
	'Magnitude',
	'Region',
	'image',
	'station',
	'comp',
	'DIS',
	'AZM',
	'ARR_TIME',
	'RES',
	'PHASE',
	'date_posted']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



def about(request):
    return render(request, 'testdb/about.html', {'title': 'About'})

def seismic(request):
    return render(request, 'testdb/Seismic.html', {'title': 'Seismic'})


