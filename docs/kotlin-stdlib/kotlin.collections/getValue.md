

# getValue

Returns the value of the property for the given object from this read-only map.

```kotlin
inline operator fun <V, V1 : V> Map<in String, V>.getValue(thisRef: Any?, property: KProperty<*>): V1(source)
```

```kotlin
class User(data: Map<String, Any>) {
    val name: String by data
    val age: Int by data
}

fun main() {
    val user = User(
        mapOf(
            "name" to "Bob",
            "age" to 25
        )
    )
    println(user.name)  // Bob
    println(user.age)   // 25
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/get-value.html)

    