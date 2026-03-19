

# takeLast

Returns a subsequence of this char sequence containing the last n characters from this char sequence, or the entire char sequence if this char sequence is shorter.

```kotlin
fun CharSequence.takeLast(n: Int): CharSequence(source)
```

```kotlin
fun main() {
    val text = "Hello, world!"
    val lastFive = text.takeLast(5)
    println(lastFive) // Output: world!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/take-last.html)

    