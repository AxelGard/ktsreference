

# isNotEmpty

Returns true if this char sequence is not empty.

```kotlin
inline fun CharSequence.isNotEmpty(): Boolean(source)
```

```kotlin
fun main() {
    val nonEmpty = "Kotlin"
    val empty = ""

    println(nonEmpty.isNotEmpty()) // true
    println(empty.isNotEmpty())    // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-not-empty.html)

    