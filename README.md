# Ftech_Training
## Tuần 1
 * Django
   * View, Route
   * App/Blueprint
   * Template"
   * File báo cáo trong : Reports/Week3_Django.md
   * Demo test : django/mysite/polls
## Tuần 2 
* Django-restframework
		Serializers : cho phép dữ liệu phức tạp(query...)<-> đơn giản (json,xml).
    + dữ liệu từ quyery set qua nó được chuyển sang dạng đơn giản ,ngược lại dữ liệu 
đơn giản được chuyển thành dữ liệu để lưu vào model
    + có phần giống với form
    + get,post: lấy toàn bộ(get) và thêm(post)
    + get,delete,put+id: lấy một đối tượng cụ thể(get),xoá đối tượng(delete),cập nhật đối tượng(put)
        +put: Model(object cũ,data mới) -> save()
    +data:
        + query->json: data=Serializers(query,many=True(nếu có nhiều object))-> data.data
        + json->model : data=Serializers(data=request.data) -> data.data['key']
    +is_valid(raise_exception=True): thông báo lỗi cho từng trường 
    +validation:
        +validate_name: một trường cụ thể
            +Nếu  <field_name>được khai báo trên bộ tuần tự với required=False thì bước xác thực này sẽ không diễn ra nếu trường không được bao gồm,nếu muốn (validators=[validate_name])
        + validate : các trường với nhau
    +depth:đối số độ sâu
    +Các tuỳ  chọn field:
        + read_only: chỉ đọc ,mặc định là False
        + write_only : chỉ ghi ,không hiển thị khi biểu diễn mặc địng là False
        + required : cho phép trống hay không :mặc định là True *
        + allow_null: chấp nhận giá trị None được chuyển đến(True),mặc định là False
        + allow_blank: cho phép để trống trường
        + default: mặc định nếu khôn được cung cấp
        + initial : truyền trước một giá trị nào đó trong html
        + trong ModelSerializers ,nếu muốn thêm các tuỳ chọn cho trường  :
            +extra_kwargs = {
            'fields_name': {
                'write_only,...': True
            }
            }

    + Các mối quan hệ
        + StringRelatedField : dùng __str__ để thể hiện
        + PrimaryKeyRelatedField : dùng id để thể hiển
        + HyperlinkedRelatedField: sử dụng một kết nối
        + SlugRelatedField(slug_field='?') : dùng một trường để thể hiện
        + HyperlinkedIdentityField
        + Mối quan hệ lồng ghép: trường này liên kết với một class khác


   + PageNumberPagination
        + cấu hình trong setting hoặc gọi trong class pagination_class
        + page_size:  kích thước trang. Nếu được đặt, ghi đè PAGE_SIZE cài đặt. Mặc định có cùng giá trị với PAGE_SIZE khóa cài đặt.
        + page_query_param: Giá trị chuỗi cho biết tên của tham số truy vấn để sử dụng cho điều khiển phân trang.
        + page_size_query_param: Nếu được đặt, đây là giá trị chuỗi cho biết tên của tham số truy vấn cho phép khách hàng đặt kích thước trang trên cơ sở mỗi yêu 	cầu. Mặc định là None, cho biết rằng máy khách có thể không kiểm soát kích thước trang được yêu cầu.
        + max_page_size: Nếu được đặt, đây là giá trị số cho biết kích thước trang được yêu cầu tối đa cho phép. Thuộc tính này chỉ hợp lệ nếu page_size_query_paramcũng được đặt.
        + last_page_strings: Một danh sách hoặc nhiều giá trị chuỗi cho biết các giá trị có thể được sử dụng với page_query_param để yêu cầu trang cuối cùng trong tập hợp. Mặc định là('last',)
        + template: Tên của mẫu để sử dụng khi hiển thị các điều khiển phân trang trong API có thể duyệt. Có thể được ghi đè để sửa đổi kiểu kết xuất hoặc đặt thành None tắt hoàn toàn các điều khiển phân trang HTML. Mặc định là "rest_framework/pagination/numbers.html".

    + View:
        GenericViewset: có sẵn các hàm 
            + queryset
            + serializer_class
        ModelViewset: 
            + kế thừa từ các lớp mixin và GenericViewset do đó cũng phải cung cấp thêm hai biến trên
            + create(), retrieve(), update()_cập nhật tất cả,partial_update()_cập nhật một phần, destroy(), list()

        Router:
            router.register() -> include(router.url)



    + Sql:
        Join: Select From table1 (join) table2 on ?
            + inner: INNER JOIN : chung của hai bảng
            + left join: LEFT [OUTER] JOIN : toàn bộ bảng 1 và một phần bảng 2 khớp với điều kiện
            + right join : RIGHT [OUTER] JOIN : toàn bộ bảng 2
            + full : FULL [OUTER] JOIN  : cả hai bảng 
            -> không có thì là Null


    + LAG ( expression [, offset [, default] ] ) OVER ( [ query_partition_clause ] order_by_clause ) : lấy dòng trước đó
        +expression : tên cột , hoặc các biểu thức trả về một giá trị
        +offset: bước nhảy
        + default
        + query_partition_clause : PARTITION BY ? : chia thành các nhóm 
        + order_by_clause : ORDER BY ? : xác định thứ tự trong mỗi phân vùng
            + sắp xếp trước ->lấy bản ghi trước đó
        +Lead : Lấy dòng sau

    + Case
        + Simple case:so sánh một biểu thức với một bộ các biểu thức đơn giản để xác định kết quả.
            + CASE bieuthuc_dauvao
                WHEN bieuthuc_1 THEN ketqua_1
                WHEN bieuthuc_2 THEN ketqua_2
                ...
                WHEN bieuthuc_n THEN ketqua_n
                ELSE ketqua_khac
                END
        + Searched case :đánh giá một bộ các biểu thức Boolean để xác định kết quả.
                +CASE
                WHEN dieukien_1 THEN ketqua_1
                WHEN dieukien_2 THEN ketqua_2
                ...
                WHEN dieukien_n THEN ketqua_n
                ELSE ketqua_khac
                END

    + Có thể sử dụng trong order by và group by



    + Swagger:
    + https://swagger.io/
    + https://swagger.io/tools/swagger-codegen/
    + https://spago.ftech.ai/swagger/
    + drf yasg
    + https://drf-yasg.readthedocs.io/en/stable/
