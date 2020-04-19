<script type="text/javascript">
	$(document).ready(function(){
    beginning_date = Date.parse('{{task.beginning_date}}');
    $('#beginning_date').pickadate('picker').set('select', beginning_date, {format: 'dd/mm/yyyy'}).trigger('change')
    });
</script>


<script type="text/javascript">
		$(document).ready(function(){
            $('.collapsible').collapsible();
            $('select').material_select();
            $(".button-collapse").sideNav();
        });

        $('.datepicker').pickadate({
            selectMonths: true, 
            selectYears: 15, 
            today: 'Today',
            clear: 'Clear',
            close: 'Ok',
            closeOnSelect: false 
        });

        
        $(document).ready(function(){
            $('.slider').slider();
        });

document.getElementById("matfix").addEventListener("click", function(e) {
	e.stopPropagation();
});

	</script>