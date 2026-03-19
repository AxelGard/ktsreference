

# isNullOrEmpty

Returns true if this nullable array is either null or empty.

```kotlin
inline fun Array<*>?.isNullOrEmpty(): Boolean(source)
```

```kotlin
fun main() {
    val array1: Array<String>? = null
    val array2: Array<String>? = arrayOf()
    val array3: Array<String>? = arrayOf("a", "b")

    println(array1.isNullOrEmpty()) // true
    println(array2.isNullOrEmpty()) // true
    println(array3.isNullOrEmpty()) // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/is-null-or-empty.html)

    