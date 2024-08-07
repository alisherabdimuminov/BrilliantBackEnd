from django.urls import path

from .views import (
    # inputs get
    get_inputs_by_date,
    get_inputs_count_by_date,
    #  inputs post
    post_inputs,

    # outputs get
    get_outputs_by_date,
    get_outputs_count_by_date,
    # outputs post
    post_outputs,

    # group inputs get
    get_group_inputs_by_date,
    get_group_inputs_count_by_date,
    # group inputs post
    post_group_inputs,

    # all get
    all_by_date,

    # statistics
    get_statistics_by_date,

    # workers
    get_faces,
    get_workers,
    create_customer_face,
    create_worker_face,
    get_workers_statistics_by_date,

    get_customers_count,
    get_workers_count,
)


urlpatterns = [
    # inputs
    path("inputs/count/", get_inputs_count_by_date, name="inputs_count"),
    path("inputs/all/", get_inputs_by_date, name="inputs_by_date"),
    path("inputs/create/", post_inputs, name="create_input"),

    # outputs
    path("outputs/count/", get_outputs_count_by_date, name="outputs_count"),
    path("outputs/all/", get_outputs_by_date, name="outputs_by_date"),
    path("outputs/create/", post_outputs, name="create_output"),

    # group inputs
    path("group_inputs/count/", get_group_inputs_count_by_date, name="group_inputs_count"),
    path("group_inputs/all/", get_group_inputs_by_date, name="group_inputs_by_date"),
    path("group_inputs/create/", post_group_inputs, name="create_group"),

    # all by date
    path("all/", all_by_date, name="all_by_date"),

    # statistics
    path("statistics/", get_statistics_by_date, name="statistics"),
    path("statistics/workers/", get_workers_statistics_by_date, name="worker_statistics"),

    # workers
    path("faces/", get_faces, name="faces"),
    path("workers/", get_workers, name="workers"),
    path("faces/create/customer/", create_customer_face, name="create_customer_face"),
    path("faces/create/worker/", create_worker_face, name="create_worker_face"),

    path("workers/count/", get_workers_count, name="workers_count"),
    path("customers/count/", get_customers_count, name="customers_count"),
]