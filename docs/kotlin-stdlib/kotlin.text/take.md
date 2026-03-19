

# take

Returns a subsequence of this char sequence containing the first n characters from this char sequence, or the entire char sequence if this char sequence is shorter.

```kotlin
fun CharSequence.take(n: Int): CharSequence(source)
```

```kotlin
fun main() {
    val text = "Hello, world!"

    // Take the first 5 characters
    println(text.take(5))   // Output: Hello

    // Take more characters than the string length
    println(text.take(20))  // Output: Hello, world!
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/take.html)

    