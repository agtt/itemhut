<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% include('global/header.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')
% include('global/top_nav.tpl')


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   	<ul class="vertical menu">
			<li>
				<a href = "/products">All</a>
			</li>
			<li>
				<a href = "/products/bandm">My B&M Store</a>
			</li>
			<li>
				<a href = "/products/website">My website</a>
			</li>
			<li>
				<a href = "/products/amazon">Amazon</a>
			</li>
			<li>
				<a href = "/products/amazon">Amazon</a>
			</li>
			<li>
				<a href = "/products/ebay">eBay</a>
			</li>
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">
	         <p>stuff here</p>
	   </div>      
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')