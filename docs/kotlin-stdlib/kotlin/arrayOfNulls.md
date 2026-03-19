

# arrayOfNulls

Returns an array of objects of the given type with the given size, initialized with null values.

```kotlin
expect fun <T> arrayOfNulls(size: Int): Array<T?>(source)
```

```kotlin
// Create an array of 3 nullable Strings, all initialized to null
val names: Array<String?> = arrayOfNulls(3)

// Assign values to some elements
names[0] = "Alice"
names[2] = "Bob"

// Print the array contents
println(names.contentToString())   // Output: [Alice, null, Bob]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/array-of-nulls.html)

    