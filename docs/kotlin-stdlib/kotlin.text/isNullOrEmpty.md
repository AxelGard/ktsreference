

# isNullOrEmpty

Returns true if this nullable char sequence is either null or empty.

```kotlin
inline fun CharSequence?.isNullOrEmpty(): Boolean(source)
```

```kotlin
fun main() {
    val text1: CharSequence? = null
    val text2: CharSequence? = ""
    val text3: CharSequence? = "Hello, Kotlin!"

    println(text1.isNullOrEmpty()) // true
    println(text2.isNullOrEmpty()) // true
    println(text3.isNullOrEmpty()) // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-null-or-empty.html)

    