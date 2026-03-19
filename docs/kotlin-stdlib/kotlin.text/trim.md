

# trim

Returns a subsequence of this char sequence having leading and trailing characters matching the predicate removed.

```kotlin
inline fun CharSequence.trim(predicate: (Char) -> Boolean): CharSequence(source)
```

```kotlin
fun main() {
    val str = "xxxHello, World!!!xxx"
    val trimmed = str.trim { it == 'x' || it == '!' }
    println(trimmed)  // prints: Hello, World
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim.html)

    