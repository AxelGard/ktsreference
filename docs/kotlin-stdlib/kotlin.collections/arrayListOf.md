

# arrayListOf

Returns an empty new ArrayList.

```kotlin
inline fun <T> arrayListOf(): ArrayList<T>(source)
```

```kotlin
fun main() {
    // Create an empty ArrayList of strings
    val names = arrayListOf<String>()

    // Add elements to the list
    names.add("Alice")
    names.add("Bob")
    names.add("Charlie")

    // Print the list
    println(names)   // Output: [Alice, Bob, Charlie]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/array-list-of.html)

    