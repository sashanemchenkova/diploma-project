   {% if user.is_authenticated %}
            <form action="{% url 'logout' %}?next={{ request.path }}" method="post"
                  class="">
                {% csrf_token %}
                    <input type="submit" value="Logout" class="btn btn-danger"/>
            </form>
        {% else %}
            <a href="{% url 'login' %}?next={{ request.path }}"
                   class="btn btn-info">Login</a>
        {% endif %}
