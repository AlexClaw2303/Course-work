$(document).ready(function () {
	/**
	 * При прокрутке страницы, показываем или срываем кнопку
	 */
	$(window).scroll(function () {
		// Если отступ сверху больше 50px то показываем кнопку "Наверх"
		if ($(this).scrollTop() > 50) {
			$("#button-up").fadeIn();
		} else {
			$("#button-up").fadeOut();
		}
	});

	/** При нажатии на кнопку мы перемещаемся к началу страницы */
	$("#button-up").click(function () {
		$("body,html").animate(
			{
				scrollTop: 0,
			},
			1000
		);
		return false;
	});
});
$(function () {
	$('a[href^="#"]').on("click", function (event) {
		// отменяем стандартное действие
		event.preventDefault();

		var sc = $(this).attr("href"),
			dn = $(sc).offset().top;
		/*
		 * sc - в переменную заносим информацию о том, к какому блоку надо перейти
		 * dn - определяем положение блока на странице
		 */

		$("html, body").animate({ scrollTop: dn }, 1000);

		/*
		 * 1000 скорость перехода в миллисекундах
		 */
	});
});
