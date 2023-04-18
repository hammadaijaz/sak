frappe.pages['sales_dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Sales Dashboard',
		single_column: true
	});

	wrapper = $(wrapper).find('.layout-main-section');

	var make_field = function(class_name, fieldtype, label, options, readonly=0){
		var description = "";
		page[class_name] = frappe.ui.form.make_control({
			df: {
				fieldtype: fieldtype,
				label: label,
				fieldname: class_name,
				options: options,
				read_only : readonly,
				description : description,
				onchange: () => {
					var value = null;
					if(fieldtype != "Select"){
						value = $('input[data-fieldname='+class_name+']').val();
						// if(fieldtype == "Date"){
						// 	value = $('input[data-fieldname='+class_name+']').val();
						// }
					}
					else {
						value = $("."+class_name).find('.control-value').text();
						// $( "."+class_name+ "option:selected" ).text();
					}
					filters[class_name] = value
					load_chart_data()
				}
			},
			parent: $('.'+class_name),
			render_input: true
		});
	}

	var filters = {}

	wrapper.append(`
			<div class="row">
				<div class="period_group col-md-4"></div>
		`)

	make_field("period_group", "Select", "Group By", ["Daily", "Weekly", "Monthly", "Yearly"])

	wrapper.append(`<div class="row" id="page-content">
		<div class="col-md-4 chart1"></div>
		<div class="col-md-4 chart2"></div>
		<div class="col-md-4 chart3"></div>
		<div class="col-md-4 chart4"></div>
		<div class="col-md-4 chart5"></div>
		<div class="col-md-4 chart6"></div>
		<div class="col-md-4 chart7"></div>
		<div class="col-md-4 chart8"></div>
		<div class="col-md-4 chart9"></div>
		<div class="col-md-4 chart10"></div>
		<div class="col-md-4 chart11"></div>
		<div class="col-md-4 chart12"></div>
		</div>`)

	var load_chart_data = function(){
		frappe.call({
			method: "sak.sak.page.sales_dashboard.sales_dashboard.get_sales_data",
			args: {filters: filters},
			callback: function(r) {
				const chart_data = r.message;

				const graph1 = new frappe.Chart(".chart1", {
					title: "POS-Terminal-North",
					data: chart_data[0],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});
				const graph2 = new frappe.Chart(".chart2", {
					title: "POS-Terminal-North Without Tax",
					data: chart_data[1],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});

				const graph3 = new frappe.Chart(".chart3", {
					title: "POS-Terminal-Gulshan",
					data: chart_data[2],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});

				const graph4 = new frappe.Chart(".chart4", {
					title: "POS Terminal Gulshan Without Tax",
					data: chart_data[3],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});

				const graph5 = new frappe.Chart(".chart5", {
					title: "POS-Terminal-Sehar",
					data: chart_data[4],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});

				const graph6 = new frappe.Chart(".chart6", {
					title: "POS-Terminal-Sehar Without Tax",
					data: chart_data[5],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});
				const graph7 = new frappe.Chart(".chart7", {
					title: "POS-Terminal-Badar",
					data: chart_data[6],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});
				const graph8 = new frappe.Chart(".chart8", {
					title: "POS-Terminal-Badar Without Tax",
					data: chart_data[7],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});

				const graph9 = new frappe.Chart(".chart9", {
					title: "POS Terminal-Bahadurabad",
					data: chart_data[8],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});

				const graph10 = new frappe.Chart(".chart10", {
					title: "POS Terminal Bhadrabad Without Tax",
					data: chart_data[9],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});

				const graph11 = new frappe.Chart(".chart11", {
					title: "POS Terminal - Johar",
					data: chart_data[10],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});

				const graph12 = new frappe.Chart(".chart12", {
					title: "POS Terminal Johar Without Tax",
					data: chart_data[11],
					type: "pie",
					height: 360,
					colors: ['#FFBF00', '#40E0D0']
				});

				// setTimeout(function () { graph1.draw(!0);}, 1);
				// setTimeout(function () { graph2.draw(!0);}, 1);
				// setTimeout(function () { graph3.draw(!0);}, 1);
				// setTimeout(function () { graph4.draw(!0);}, 1);
				// setTimeout(function () { graph5.draw(!0);}, 1);
				// setTimeout(function () { graph6.draw(!0);}, 1);
				// setTimeout(function () { graph7.draw(!0);}, 1);
				// setTimeout(function () { graph8.draw(!0);}, 1);
				// setTimeout(function () { graph9.draw(!0);}, 1);
				// setTimeout(function () { graph10.draw(!0);}, 1);
				// setTimeout(function () { graph11.draw(!0);}, 1);
				// setTimeout(function () { graph12.draw(!0);}, 1);
			}
		})
	}

	load_chart_data()
	$(document.body).addClass('full-width');
}