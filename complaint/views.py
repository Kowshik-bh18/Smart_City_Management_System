from django.shortcuts import render, redirect, get_object_or_404
from .models import LocationImage
from .forms import LocationImageForm
from django.contrib.auth.decorators import login_required

# List view
@login_required
def image_list(request):
    # Fetch all images for the logged-in user or superusers
    images = LocationImage.objects.filter(user=request.user) if not request.user.is_superuser else LocationImage.objects.all()
    return render(request, 'complaint/image_list.html', {'images': images})

# Create view
@login_required
def image_upload(request):
    if request.method == 'POST':
        form = LocationImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user  # Assign the current user to the image
            obj.save()
            return redirect('complaint:image_list')  # Redirect to image list after upload
    else:
        form = LocationImageForm()
    return render(request, 'complaint/image_form.html', {'form': form, 'action': 'Upload'})

# Update view
@login_required
def image_edit(request, pk):
    # Fetch image by pk and ensure it belongs to the current user
    image = get_object_or_404(LocationImage, pk=pk, user=request.user)
    if request.method == 'POST':
        form = LocationImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('complaint:image_list')  # Redirect after successful update
    else:
        form = LocationImageForm(instance=image)  # Populate the form with existing data
    return render(request, 'complaint/image_form.html', {'form': form, 'action': 'Update'})

# Delete view
@login_required
def image_delete(request, pk):
    # Fetch the image and ensure it belongs to the current user
    image = get_object_or_404(LocationImage, pk=pk, user=request.user)
    if request.method == 'POST':
        image.delete()  # Delete the image after POST request
        return redirect('complaint:image_list')  # Redirect after deletion
    return render(request, 'complaint/image_confirm_delete.html', {'image': image})  # Confirm before deletion

