

# toBoolean

Returns true if this string is not null and its content is equal to the word "true", ignoring case, and false otherwise.

```kotlin
expect fun String?.toBoolean(): Boolean(source)
```

fun main() {
    val a = "true".toBoolean()
    val b = "FALSE".toBoolean()
    val c: String? = null
    val d = c.toBoolean()

    println(a) // true
    println(b) // false
    println(d) // false
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-boolean.html)

    