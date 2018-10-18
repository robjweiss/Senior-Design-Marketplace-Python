function projectCard(id, title, desc, date, locked) {
return `
<div class="card">
	<div class="card-body">
		<h5 class="card-title">${locked}${title}</h5>
		<p class="card-text">${desc}</p>
		<p class="card-text"><small class="text-muted">Last updated ${date}</small>
	</div>
	<div class="card-footer">
		<a href="#" class="btn btn-primary disabled">Apply</a>
		<a href="#" class="btn btn-primary" data-toggle="modal" data-target="#modal${id}">More Info</a>
	</div>
</div>`;
}

function projectModal(id, title, desc, date, views, author, locked) {
	return `
<div class="modal fade bd-example-modal-lg" id="modal${id}" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
	<div class="modal-dialog modal-lg">
	<div class="modal-content">
	<div class="modal-header">
	<h5 class="modal-title" id="exampleModalLabel">${locked}${title} <button type="button" class="close"  id="favButton" style="padding-left:0.2rem !important; color:red !important;"><span id="favText" class="material-icons">favorite_border</span></button></h5>
	<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
	</div>
		
	<div class="modal-body">
		<ul class="nav nav-pills">
		<li class="nav-item">
			<a class="nav-link active" id="generalTab" data-toggle="tab" href="#general" role="tab" aria-controls="general" aria-selected="true">General</a>
		</li>
		<li class="nav-item">
			<a class="nav-link" id="lookingTab" data-toggle="tab" href="#lookingFor" role="tab" aria-controls="lookingTab" aria-selected="false">Looking for</a>
		</li>
		<li class="nav-item">
			<a class="nav-link" id="memberTab" data-toggle="tab" href="#member" role="tab" aria-controls="memberTab" aria-selected="false">Current Members</a>
		</li>
		</ul>
	<div class="modal-content-tldr"><span class="infoSpan"><span class="material-icons" style="color:red">whatshot</span> ${views} views</span><span class="infoSpan">Created by: <a class='regularLink'>${author}</a> ${date}</span><span class="infoSpan-last"><span class="material-icons" style="color:red">favorite</span>xxx</span></div>
	<div class="container-fluid">
	<div class="tab-content" id="myTabContent">
	<!--General-->
	<div class="tab-pane fade show active modal-content-true" id="general" role="tabpanel" aria-labelledby="generalTab">
		content
	</div>
	<!--Looking For-->
	<div class="tab-pane fade modal-content-true" id="lookingFor" role="tabpanel" aria-labelledby="lookingTab">
	<div class="row">
		<table class="table table-sm" style="width:50%">
			<thead>
				<tr>
					<th scope="col">Major</th>
					<th scope="col">Total Spots Remaining</th>
				</tr>
				</thead>
			<tbody>
			<tr>
				<th scope="row">Chemical Engineering</th>
				<td style="color:red;"><strong>2/2</strong></td>
			</tr>
			<tr>
				<th scope="row">Software Engineering</th>
				<td style="color:green;">0/3</td>
			</tr>
			<tr>
				<th scope="row">Naval Engineering</th>
				<td style="color:green;">1/4</td>
			</tr>
			</tbody>
			</table>
			</div>
			</div>
			<!--Member Info-->
			<div class="tab-pane fade modal-content-true" id="member" role="tabpanel" aria-labelledby="memberTab">
			<!--NEED A ROW EVERY 3 MEMBERS-->
			<div class="row">
			<div class="col-md-4 pictureAlign">
			<img class="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
			<h5>Kevin Hockenjos</h5>
			</div>
			<div class="col-md-4 pictureAlign">
			<img class="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
			<h5>Taylor Swift</h5>
			</div>
			<div class="col-md-4 pictureAlign">
			<img class="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
			<h5>The Rock</h5>
			</div>
			</div>
			
			<div class="row">
			<div class="col-md-4 pictureAlign">
			<img class="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
			<h5>schad</h5>
			</div>
			<div class="col-md-4 pictureAlign">
			<img class="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
			<h5>brad</h5>
			</div>
			</div>
			
			</div>
		</div>
		
		</div>
		</div>
	  
		<div class="modal-footer">
			<button type="button" class="btn btn-primary" data-dismiss="modal">Apply</button>
		</div>
	  
    </div>
  </div>
</div>`;
}