

# subSequence

Returns a subsequence of this char sequence specified by the given range of indices.

```kotlin
fun CharSequence.subSequence(range: IntRange): CharSequence(source)
```

```kotlin
fun main() {
    val original = "Kotlin is fun!"
    val sub = original.subSequence(7..8)
    println(sub) // Output: is
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/sub-sequence.html)

    